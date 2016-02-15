---
layout: docsp
---
## Basics

Hi! You are probably here because you want to use PipeScript for some data analysis task. Let's get started!

Datapoint
=============

The data that PipeScript accepts consists of a stream of Datapoints, each of which has the following structure:

```
{
    "t": floating point timestamp (unix time in seconds),
    "d": the datapoint's data content.
}
```


Data Conversion
----------------
When importing data to ConnectorDB, or when the `pipes` executable attempts to convert your data, it is always converted into the above format.

For example, if you have a CSV file:

```
timestamp,                       steps_taken, activity_type
Tuesday, 12-Jan-16 00:27:09 UTC,         234,        walking
...
```

then the first datapoint of your stream will be

```json
{
    "t": 1452558429.0,
    "d": {
           "steps_taken": "234",
           "activity_type": "walking"
         }
}
```

Don't worry if certain fields are not the correct type ("steps_taken" is "234", which is a string). PipeScript transparently converts data into the relevant types during processing.

Starting Out
====================

For the next few examples, we will use the following data:

```json
[{"t": 123, "d": 2},
{"t": 124, "d": "1"},
{"t": 124, "d": 0.1},
{"t": 124, "d": -50},
{"t": 124, "d": "true"}]
```

This isn't particularly realistic data, since the time stamp is weird, and there is this "true" in the dataset, but it will do for our purposes.

Comparisons
--------------

To start out, let's see which datapoints have their data >= 1.

```
$ >= 1
```

If you are familiar with programming, this is just a simple comparison statement using a weird "$" symbol.

Running the above PipeScript returns:

```json
[{"t": 123, "d": true},
{"t": 124, "d": true},
{"t": 124, "d": false},
{"t": 124, "d": false},
{"t": 124, "d": true}]
```

### So what happened here?

PipeScript is a stream processing language. This means that your script is executed in order for every datapoint individually. Using the built-in `$` transform, which is the identity (ie, it always just returns the datapoint it gets), we can get our result in the data section of a new stream of datapoints.

Also notice that the boolean was automatically converted to a number. In PipeScript, `false==0` and `true==1`.

Logic
-------------

Logic operations (and/or/not) are built into PipeScript. This allows you to use them as you would in python:

```
$ < 0 or not $ < 1
```

```json
[{"t": 123, "d": true},
{"t": 124, "d": true},
{"t": 124, "d": false},
{"t": 124, "d": true},
{"t": 124, "d": true}]
```

## Algebra

PipeScript also supports basic algebra. In particular, `+-/*%^` are all built into the language, with `x^y` meaning `pow(x,y)`.

```
($+5)/2
```

gives:

```json
[{"t": 123, "d": 3.5},
{"t": 124, "d": 3},
{"t": 124, "d": 2.55},
{"t": 124, "d": -22.5},
{"t": 124, "d": 3}]
```

By itself, being able to compare and add things to datapoints isn't particularly enlightening, but it becomes useful when used for filtering data:

## Filtering Data

```
if $ >= 1
```

In PipeScript, the `if` statement is really a filter. It permits only those datapoints to pass that have met the given condition. When run on our original dataset above, we get:

```json
[{"t": 123, "d": 2},
{"t": 124, "d": 1},
{"t": 124, "d": "true"}]
```

Another, probably more clear, way of writing this same transform is:
```
if($>=1)
```
Transforms can be called using both a bash-like syntax `function arg1 arg2 arg3`, and a standard function-call syntax: `function(arg1,arg2,arg3)`. You can even put entire pipelines into arguments of a transform (more on that later).

Using Transforms
=======================

PipeScript has many built-in transform functions. A list of the ones available in the most recent version of ConnectorDB is available [here](https://connectordb.github.io/docs/transforms.html).

To get you started, here are a couple particularly useful scripts that don't require knowledge of pipelines:

```
if last
```
Only returns the last datapoint

```json
[{"t": 124, "d": "true"}]
```

```
sum
```

```json
[{"t": 123, "d": 2},
{"t": 124, "d": 3},
{"t": 124, "d": 3.1},
{"t": 124, "d": -46.9},
{"t": 124, "d": -45.9}]
```


While already pretty useful, the real power of PipeScript comes from combining the transforms into pipelines, as we will do in the [next tutorial](./pipeline.html).
