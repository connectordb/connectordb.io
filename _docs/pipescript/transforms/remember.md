# remember
*Behaves as a single-datapoint memory cell, which is reset when its first argument is true.*

`remember` allows you to save a chosen datapoint. Whenever the argument of `remember` is `true`, it saves the current datapoint, and keeps repeating it while the argument is `false`.

An example will explain this very nicely. If your data is:
```
20,40,-50,20,-10,3,-9,40,50
```

then the transform `remember($ < 0)` will return:
```
20,20,-50,-50,-10,-10,-9,-9,-9
```

The reason the `20` is repeated at the beginning, despite it being positive, is because `remember` is always initialized with your first datapoint.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The statement to check for truth. If true, it will remember the current datapoint</td><td>False</td><td>False</td><td>False</td><td></td></tr><tr><td>2</td><td>Optional, if this is set, then the result of this argument is stored instead of the datapoint</td><td>True</td><td>False</td><td>False</td><td>None</td></tr></table>
