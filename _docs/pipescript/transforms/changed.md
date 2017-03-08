<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# changed
*Returns true if the datapoint has a different value from the previous one*

The changed transform returns true if the current datapoint's data is different from the previous datapoint.

Given the following data:
```
1,2,3,3,4
```
running the `changed` transform on it will result in:
```
true,true,true,false,true
```

### Usage

The `changed` transform is useful whenever you don't care about the specific datapoints,
but when they change with respect to a certain metric.

Suppose you have a stream of activities gathered by a phone:
```
walking,walking,still,still,still,walking,walking
```

You usually care about the transitions between activities:
```
if changed
```
gives:
```
walking,still,running
```

Remember that each datapoint comes with a timestamp, so the length of each activity can be extracted by looking at the timestamp differences.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

