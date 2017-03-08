<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# append
*Appends data into one large string*

`append` is a transform made for strings - it appends all of the data it has seen so far into one large string:

Suppose your stream is:
```json
["hello ","world",24,true]
```

Then running the transform `append` on your data will give you:
```json
["hello ","hello world","hello world24","hello world24true"]
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td>{"type": "string"}</td></tr></table>

