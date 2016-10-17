# set
*Allows setting object values*

The `set` transform allows to add/modify values in an object-formatted datapoint.

```json
[
  {},
  {"foo": "baz"},
  {"a": 1,"b":2}
]
```
With the above data, and the transform `set("foo","bar")`, we get:

```json
[
  {"foo":"bar"},
  {"foo": "bar"},
  {"a": 1,"b":2,"foo":"bar"}
]
```

Remember that PipeScript has native support for json-formatted data. You can directly set objects with transforms like the following:
```
{"foo": "bar", "a": $("a")}
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The name of field to set</td><td>False</td><td>True</td><td>False</td><td></td></tr><tr><td>2</td><td>The value to set the field to</td><td>False</td><td>False</td><td>False</td><td></td></tr></table>
