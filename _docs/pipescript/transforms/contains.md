<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# contains
*Returns true if the given string is found in the datapoint string*

`contains` permits you to check if a datapoint with a string data value contains the given substring:

```json
["Hello World!","hello world","hi there"]
```

Running the transform `contains("World")` will give:
```json
[true,false,false]
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td>{"type": "boolean"}</td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The string to search for</td><td>False</td><td>True</td><td>False</td><td></td></tr></table>
