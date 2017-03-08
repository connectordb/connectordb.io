<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# while
*Equivalent to a while loop that runs while the first argument is true. Restarts the loop when the argument is false.*

Oftentimes, you don't really want all of the raw data from your stream. You are usually interested in timed aggregations or other such things. This is the main use case of the `while` transform.

This transform performs a while loop on its second argument while its first argument is true. When the first argument becomes false, it returns the resulting datapoint, and begins the next loop.

This allows summing up datapoints over specified time periods. For example, `day==next:day` is true if the current datapoint and next datapoint in the stream ave timestamps from the same day.

This allows you to write a transform performing an aggregation per day:

```
while(day==next:day, sum)
```

The above transform loops through datapoints while they come from the same day, and sums their values. Once the next datapoint is a different day than the current one, it ends the while loop, and returns the sum, giving the sum of all datapoints that day. It then starts a loop for the next day.

The transform can also be used for smoothing. Suppose you want to smooth your data every three datapoints:

```
while(count%3!=0, mean)
```

This returns the mean of every consecutive three datapoints, making it easy to do a basic smoothing procedure.


## Advanced Usage

The transform can also be used to implement error bars:

```
while(day==next:day, {"max": max, "min": min, "mean": "mean"})
```

This transform returns the mean, max and min datapoint for the day all at once, allowing to plot with error bars.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The statement to check for truth</td><td>False</td><td>False</td><td>False</td><td></td></tr><tr><td>2</td><td>pipe to run, and to reset when the first arg is false</td><td>False</td><td>False</td><td>True</td><td></td></tr></table>
