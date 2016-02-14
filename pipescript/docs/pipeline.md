---
layout: docsp
---
## Pipeline

In the [last tutorial](./basics.html), the basic element of PipeScript was introduced. The Transform.

To reiterate in more detail, a Transform can be:

- An algebraic or logical statement: `($ + 5)/2 > 5 or $ < 3`
- A transform function call (`if($>5)` or equivalently `if $>5`. Both function-call and bash-like syntax are allowed.)
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
},]
```

We want to get the **total number of steps we took while running**. We cannot do this with one transform, but by chaining together a couple simple transforms, we can get there!

First off, we want to pass through only the datapoints where we were running:

```
if $("activity") == "running"
```

Notice that the identity operator `$` accepts an argument - it allows you to return a sub-object of your Datapoint. Our result is:
```json
[
{
    "t": 2,
    "d": {
          "steps": 10,
          "activity": "running",
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
Now, let's extract the number of steps from the json object:

```
if $("activity") == "running" | $("steps")
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

Next, we want to get their sum:

```
if $("activity") == "running" | $("steps") | sum
```

```json
[{
    "t": 2,
    "d": 10
},{
    "t": 4,
    "d": 15
},]
```

This is almost there! Our second datapoint has the answer we were looking for, but the pipeline also returns the intermediate result. Therefore, we add a final transform to the end of the pipeline:

```
if $("activity") == "running" | $("steps") | sum | if last
```

```json
[{
    "t": 4,
    "d": 15
},]
```

And this is the result we were looking for!

In [the third tutorial, you will learn about one more cute feature of PipeScript: sub-pipelines](./subpipes.html).
