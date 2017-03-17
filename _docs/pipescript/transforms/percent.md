<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# percent
*Normalizes the values of a JSON object*

The `percent` transform allows you to get the percentage contribution of each element in an object. Suppose you have the following:

```json
[{
    "a": 2,
    "b": 5,
    "c": 1,
    "d": 2
}]
```

The `percent` transform will return:

```json
[{
    "a": .2,
    "b": .5,
    "c": .1,
    "d": .2
}]
```

This allows you to quickly normalize a JSON object's values.

---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td></td></tr></table>

