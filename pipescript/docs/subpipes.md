---
layout: docsp
---
## SubPipes

In the [last tutorial](./pipeline.html), we introduced pipelines.

### Sub-Pipe

Now we will go into more detail about what exactly makes up a pipeline. In particular, all arguments to each transform function are actually pipelines. For example:

```
if( ($("hi") | $("hello")) == 4 )
```

can go multiple levels into a nested object, all within a single if statement. For convenience, PipeScript also includes `:` as a pipe symbol with high prescedence (the pipe will be taken before algebra is done) which can allow you to simplify your script a bit by dropping the internal parentheses:

```
if( $("hi"):$("hello") == 4 )
```

### Pipeline Structure

Internally, PipeScript treats each argument as a separate pipeline, whose input is connected to the parent's input.


<img src="pipeline-structure.png" style="width: 100%" />


In order for the parent to always get SOME result in its argument, sub-pipelines cannot include transforms that are not One-To-One (for each datapoint that they get as input, they output one datapoint). This means that you cannot nest if transforms. Whether a specific transform is one to one is listed in its documentation.


## Hijacking

Sub-pipes are treated as full scripts, which are simply linked to the previous pipeline's output. But this linking can be "hijacked" by individual transforms. This gives transforms considerable power
over their arguments. This might be difficult to explain other than by example.

### map

The map transform is an example of a transform which hijacks its second argument. Please note that it is only lightly related to the standard `map` function in most programming languages.
It splits datapoints along its first argument, and runs independent scripts on each value:

```json
[
{
    "t": 1,
    "d": {
          "steps": 14,
          "activity": "walking"
        }
},
{
    "t": 2,
    "d": {
          "steps": 10,
          "activity": "running"
        }
},
{
    "t": 3,
    "d": {
          "steps": 12,
          "activity": "walking"
        }
},{
    "t": 4,
    "d": {
          "steps": 5,
          "activity": "running"
        }
},]
```

We found the total number of steps for "running" in the [Pipeline tutorial](pipeline.html). We can now extend that to find the number of steps for each activity!

Remember that the code was:

```
if $("activity") == "running" | $("steps") | sum | if last
```

With the map function, we can do the following:

```
map( $("activity"), $("steps"):sum )
```

which will return:

```json
[{
    "t": 4,
    "d": {
          "walking": 26,
          "running": 15
        }
},]
```

#### What just happened?

When calling `map( arg1, arg2 )`, the second argument's script was hijacked. The map transform manually took control of this argument, and generated copies of the script which were executed for each
value of arg1.

Script hijacking enables transforms to do much more powerful things. For example, the `ifelse` transform is a conditional (if statement in most programming languages). It would not be possible
to do without hijacking its arguments, since they would be executed for every datapoint by default.

### What's it good for?

A great example of the power which comes with this class of transform is aggregation queries. If we wanted to get the average number of steps per day, we could simply do:

```
map(day, $("steps"):sum ) | reduce(mean)
```

Once again, PipeScript's `reduce` function has little in common with the reduce statement in other languages. It reduces a multi-valued object to one value by performing its argument's transform
on each element, and returning the final result (last datapoint).

PipeScript's `map | reduce` is extremely useful for quick aggregation queries, despite having little in common with *real* MapReduce.
