<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# regex
*Returns true if the given regular expression matches the data string*

The regex transform checks if the data string matches the given regex.

For example, given a regex to check for valid usernames: `regex('^[a-z0-9_-]{3,16}$')`, we get:

```json
[
  "Hello World!",
  "valid_username",
  "1"
]
```

```json
[false,true,false]
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td>{"type": "boolean"}</td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The regular expression to use</td><td>False</td><td>True</td><td>False</td><td></td></tr></table>
