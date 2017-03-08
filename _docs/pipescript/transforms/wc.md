<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# wc
*Returns the number of words in the given text*

This transform counts the words in a string:

```json
["Hello World!"]
```

Running `wc` on the above returns:
```json
[2]
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td>{"type": "string"}</td><td>{"type": "integer"}</td></tr></table>

