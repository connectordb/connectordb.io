<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# sum
*Adds all of the values of the datapoints that pass through it*

The `sum` transform sums up numeric values. Given the data:
```json
[2,5,1,6]
```
running the transform `sum` will give:
```json
[2,7,8,14]
```

Since the transform returns all intermediate values, and usually we only want the total sum,
`if last` is frequently used to filter all datapoints but the final one:

```
sum | if last
```

When run on the above data, this transform returns `[14]`, which is the total sum of all datapoints in the stream.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

