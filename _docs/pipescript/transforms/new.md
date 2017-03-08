<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# new
*Returns true only when the given data was not yet seen.*

The `new` transform allows you to check if the given datapoints were seen before in the stream.

The main use case here is `if new`, which returns all the datapoints with unique data.

Suppose your data is:
```json
["foo","foo","bar","foo","bar","baz"]
```

the transform `new` will return:
```json
[true,false,true,false,false,true]
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td>{"type": "boolean"}</td></tr></table>

