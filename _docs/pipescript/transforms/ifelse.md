# ifelse
*A conditional. This is what an if statement would be in other languages.*

`ifelse` is the same type of conditional statement that you might be used to in other programming languages.

Pipescript's `if` statement is a filter, because conditionals are much less common than filters.

```
ifelse($ > 5, $-5)
```

The above will take all datapoints with data greater than 5, and decrease their value by 5. There is also an optional `else`:

```
ifelse($ > 5, $-3,$+2)
```

The above will decrease datapoints > 5 by 3, and increase all others by 2.

This permits performing conditional computation on streams.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The statement to check for truth</td><td>False</td><td>False</td><td>False</td><td></td></tr><tr><td>2</td><td>pipe to run if conditional is true</td><td>False</td><td>False</td><td>True</td><td></td></tr><tr><td>3</td><td>Pipe to run if conditional is false</td><td>True</td><td>False</td><td>True</td><td>None</td></tr></table>
