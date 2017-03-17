<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# del
*Allows deleting object values*

The `del` transform allows to delete values in an object-formatted datapoint.

```json
[
  {},
  {"foo": "baz"},
  {"a": 1,"b":2,"foo":7}
]
```
With the above data, and the transform `del("foo")`, we get:

```json
[
  {},
  {},
  {"a": 1,"b":2}
]
```

Remember that PipeScript has native support for json-like data. You can directly set objects with transforms like the following:
```json
{"foo": "bar", "a": $("a")}
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The name of field to delete</td><td>False</td><td>True</td><td>False</td><td></td></tr></table>
