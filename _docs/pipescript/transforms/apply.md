<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# apply
*Applies the given transform to each value of a JSON object*

The `apply` transform allows you to apply a script element-wise to a JSON object. For example:

```json 
[{
    "a": 5,
    "b": -2
}]
```

```
apply($+2)
```

will return:

```json 
[{
    "a": 7,
    "b": 0
}]
```

---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The script to run on each element of the object</td><td>False</td><td>False</td><td>True</td><td></td></tr></table>
