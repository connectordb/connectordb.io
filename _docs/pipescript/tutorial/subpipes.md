## SubPipes

In the <a href="pipeline.html">last tutorial</a>, we introduced pipelines.

### Sub-Pipe

Now we will go into more detail about what exactly makes up a pipeline. In particular, all arguments to each transform function are actually pipelines. For example:

```
if( (d("hi") | d("hello")) == 4 )
```

can go multiple levels into a nested object, all within a single if statement. For convenience, PipeScript also includes `:` as a pipe symbol with high prescedence (the pipe will be taken before algebra is done) which can allow you to simplify your script a bit by dropping the internal parentheses:

```
if( d("hi"):d("hello") == 4 )
```

### Pipeline Structure

Internally, PipeScript treats each argument as a separate pipeline, whose input is connected to the parent's input. 

*Note: "$" below is the same as `d`. It was used as the main identity operator in older versions of PipeScript*


<img src="/assets/docs/img/pipeline-structure.png" style="width: 100%" />


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

We found the total number of steps for "running" in the <a href="pipeline.html">pipeline tutorial</a>. We can now extend that to find the number of steps for each activity!

Remember that the code was:

```
if d("activity") == "running" | d("steps") | sum | if last
```

With the map function, we can do the following:

```
map( d("activity"), d("steps"):sum )
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

When calling `map( arg1, arg2 )`, the second argument's pipeline was hijacked. The map transform manually took control of `arg2`, and generated copies of the script for each
value of `arg1`. It then ran the scripts only on the datapoints which had the same value of `arg1`, returning only the last datapoint of each pipeline for each instantiation.

To clarify, we will see what exactly happened in the above call:

1) `map` transform saw the first datapoint, whose activity was `walking`. It created a new instance of `arg2`, `d("steps") | sum`, and ran it on the datapoint, getting `14`.
2) The next datapoint had as its activity `running`. Another instance of `d("steps") | sum` was created, which gives `10` when run on the datapoint
3) The third datapoint is `walking`. `map` already has a pipeline started for this value. Passing this datapoint through the existing pipeline we get `26` (14+12)
4) The fourth datapoint is `running`. Running the corresponding pipeline instance, we get `15`.
5) There are no more datapoints. The `map` transform returns an object with the last value of each pipeline as a result.

Script hijacking enables transforms to do much more powerful things. For example, the `ifelse` transform is a conditional (if statement in most programming languages). Such scripts would not be possible
to do without the ability to hijack their arguments, since by default the transforms passed in as arguments are executed for every incoming datapoint of the parent pipeline.

### What's it good for?

A great example of the power which comes with this class of transform is aggregation queries. If we wanted to get the average number of steps per day, we could simply do:

```
map(day, d("steps"):sum ) | reduce(mean)
```

Once again, PipeScript's `reduce` function has little in common with the reduce statement in other languages. It reduces a multi-valued object to one value by performing its argument's transform
on each element, and returning the final result (last datapoint).

PipeScript's `map | reduce` is extremely useful for quick aggregation queries, despite having little in common with *real* MapReduce.


## Multiple Values

You might want to perform multiple calculations at once in pipescript, or perhaps simply return an object. For this reason, PipeScript supports JSON-like values:

```
{"sum": sum, "total": count} | if last
```

This script will return both the sum of all of the datapoints' values, and the number of datapoints at the same time. This object support also enables you to save values for later use in the pipeline.

Finally, since scripts can get fairly complex with objects, PipeScript does accept multiline scripts. That is, the following is a valid script format:

```
if d("activity")!="still"
| {
    "total": d("steps"):sum,
    "some_random_stuff": ( d("steps") | something | something else )
}
| if last
```
