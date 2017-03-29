## Pipeline

In the <a href="basics.html">last tutorial</a>, the basic element of PipeScript was introduced. The Transform.

To reiterate in more detail, a Transform can be:

- An algebraic or logical statement: `(d + 5)/2 > 5 or d < 3`
- A transform function call (`if(d>5)` or equivalently `if d>5`. Both function-call and bash-like syntax are allowed.)
- A mixture of the two

### The Pipeline

If you have ever used bash pipes, you will be right at home in PipeScript. PipeScript is made with the same principles in mind. You create a script by piping together the outputs of several transforms, to create what we call a Pipeline.

```
a | b | c | d
```

For example, suppose that we have the following data from a fitness tracker:

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
}]
```

We want to get the **total number of steps we took while running**. We cannot do this with one transform, but by chaining together a couple simple transforms, we can get there!

First off, we want to pass through only the datapoints where we were running:

```
if d("activity") == "running"
```

Notice that the transform "d" accepts an argument - it allows you to return a sub-object of your Datapoint. Our result is:

```json
[
{
    "t": 2,
    "d": {
          "steps": 10,
          "activity": "running"
        }
},
{
    "t": 4,
    "d": {
          "steps": 5,
          "activity": "running"
        }
}]
```

We can now add a `|` after the first part of our statement, and we can perform further transforms on the result of the previous operation (shown above).
After extracting only the datapoints that have their activity as "running", we return only the "steps" portion of the datapoint:

```
if d("activity") == "running" | d("steps")
```

```json
[{
    "t": 2,
    "d": 10
},{
    "t": 4,
    "d": 5
}]
```

Remember that the result of transforms is saved in the data portion of the datapoint, so the transform `d` without any arguments passed in is really an identity (ie, running `d` as the transform of a datapoint array
will just return the same array unchanged).

We now want to get the sum of the resulting datapoints:

```
if d("activity") == "running" | d("steps") | sum
```

```json
[{
    "t": 2,
    "d": 10
},{
    "t": 4,
    "d": 15
}]
```

This is almost there! Our second datapoint has the answer we were looking for, but the pipeline also returns the intermediate results. 
Therefore, we add a final transform to the end of the pipeline to filter everything but the last datapoint:

```
if d("activity") == "running" | d("steps") | sum | if last
```

```json
[{
    "t": 4,
    "d": 15
}]
```

And this is the result we were looking for!

<a href="./subpipes.html" class="button alt">SubPipes <i class="fa fa-arrow-right"></i></a>
