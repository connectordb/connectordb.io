<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# last
*Returns true if last datapoint of a sequence, and false otherwise*

`last` is true on the last datapoint of a sequence.

It is *very* common in pipescript to end a transform with `if last` to only return the final datapoint, which contains the desired result of computation, without returning intermediate values.

```
sum | if last
```

will sum up all datapoints, and return a single datapoint with the full sum. If `if last` were not there, all intermediate values of the sum would be returned.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>True</td><td></td><td>{"type": "boolean"}</td></tr></table>

