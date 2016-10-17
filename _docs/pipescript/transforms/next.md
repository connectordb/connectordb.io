# next
*Returns the datapoint that will be next in the sequence. If given an argument, can return the nth datapoint forward.*

The `next` transform returns the datapoint *next* in the stream.

Suppose your data is`1,2,3,3,4`. The transform `$ == next` will return `false,false,true,false,false`.


The following is a verbose expansion of what is going on:
```
1==2  false
2==3  false
3==3  true
3==4  false
4==null false
```

At the end, the next transform returns null data, since its stream has ended.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>True</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The number of datapoints forward to look. Starts at 1.</td><td>True</td><td>True</td><td>False</td><td>1</td></tr></table>
