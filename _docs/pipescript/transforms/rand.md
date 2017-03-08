<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# rand
*Returns a random float in [0.0,1.0)*

The `rand` transform returns a random number if [0,1). This is useful when performing random sampling:

```
if rand < 0.7
```

will return about 70% of the datapoints randomly chosen.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td>{"type": "number","minimum": 0, "exclusiveMaximum": 1}</td></tr></table>

