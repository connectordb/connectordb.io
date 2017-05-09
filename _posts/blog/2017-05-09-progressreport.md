---
layout: post
title: "Progress Report: PipeScript"
date: 2017-05-09 00:12:00
author: Daniel
categories:
- blog
---

There were no recent updates in the repository, and one might be tempted to think that there was no progress towards the 0.3.0 release. 
While ConnectorDB work has slowed considerably in the past month due to other work, it has not stopped.
The main reason that there were no commits is that PipeScript is getting a near-total rewrite, and moving past the technical hurdles
of enabling the core new features and optimizations is *very* difficult.  I will breifly describe the parts of new PipeScript here:

## Expander Transforms

Up until now, transforms in PipeScript could only return up to 1 datapoint per input datapoint. With the new version of PipeScript,
transforms labeled as "Expanders" will be able to "expand" the streams. Why is this needed? One of the core use cases of while loops
in PipeScript is to aggregate by time. For example:

```
while(day==next:day, sum)
```

This transform would sum over datapoints which were from the same day. This works well for dense streams, where there are many datapoints per day,
but days could be skipped when there are no datapoints! To combat this situation, an `iterate` transform will expand the stream:

```
iterate(day,sum)
```

The transform returns the sum for each day, but when a day is skipped, it inserts a dummy datapoint with value 0. 
Expander transforms in general permit more advanced processing of streams, which is why they are so important to the next version of PipeScript.

## Filtering in SubTransforms

I personally really hated the fact that I needed to add `if last` to every transform to get a useful result. Currently, getting the mean of the queried datapoints,
you need to write: 

```
mean | if last
```

The reason for this is that currently PipeScript does not allow filters (tranforms that return a single answer) inside other transforms, so if the `mean` transform
returned just one datapoint, using it in a while would not be possible:

```
while(day==next:day,mean)
```

I am happy to say that in this version of PipeScript, this limitation will be removed, and the sum/mean transforms will only return one answer.
This decision is the most technically challenging of all changes to PipeScript, because transforms are permitted to peek forward into the stream.
When using a hijaking transform (such as `while`, which hijacks its second argumentto use as a script instead), the transform needs to be able to peek forward
through *future values* of a transform. For example:

```
map(weekday,if not last)
```

The above transform returns the second-to-last datapoint in each weekday. The `last` transform only knows that the datapoint is last by looking forward in its stream
and checking if there are any datapoints there. Suppose that the `last` transform wants to look to the next datapoint on a Tuesday. This means that the `map` tranform might
need to compute datapoints a whole week into the future to find the next point which is on a Tuesday. This leads to a lot of complexity, and is very difficult to get right!

This was the main source of the delay - I think I figured out how to do it correctly, but the code is yet to be written, so time will tell!

## Speed

PipeScript is slow. The current version can do a sum of 1 million datapoints in a second on my laptop (i5 4200U), which is *pathetic* when taking into account
how fast a sum can be done on the same processor when coded directly:

```
BenchmarkSum-4              	 1000000	      1077 ns/op	     328 B/op	      10 allocs/op
BenchmarkDeepSum-4          	 1000000	      1461 ns/op	     440 B/op	      14 allocs/op
BenchmarkWhile-4            	  500000	      3842 ns/op	    1045 B/op	      35 allocs/op
BenchmarkRawIteratorSum-4   	500000000	         2.82 ns/op	       0 B/op	       0 allocs/op
BenchmarkRawWhile-4         	1000000000	         2.34 ns/op	       0 B/op	       0 allocs/op
```

The goal of the new PipeScript is to be able to do a sum of 10 million datapoints in a second,
meaning that it must take at most 100ns per datapoint.

Much of the time in the old version was spent converting between types, using the [duck](https://github.com/connectordb/duck) library.
The first optimization that was done in preparation for the new PipeScript was a new method of type conversion, which is over 10 times faster,
and is called [quack](https://github.com/connectordb/duck/quack).

This by itself is a good start, but won't bring the speed up to the goal. Notice that there 10 allocations per operation in a simple sum!
My goal is to avoid allocations were possible, and currently it looks like the simple sum transform will not have any allocations during runtime!
This still needs to be benchmarked, since the current code is basically placeholder for the future functionality.

## That's it

While there are a couple more features planned, the above are things I think are on track to be implemented soon. With this upgrade, PipeScript will become a much
more powerful analysis language. Once this is finished, then only documentation and debugging are left for the 0.3.0 release of ConnectorDB!

