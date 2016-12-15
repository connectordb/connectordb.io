# filter
*Takes a json object, and considers each field to be a separate datapoint's data.
It removes all elements for which its first argument returns true (filters).*

`filter` allows you to remove values from an object based upon a condition. For example:

```json
[{
  "a": 45,
  "b": 23,
  "c": -3
}]
```

Running the transform `filter($<0)` on the above datapoint, will give an output:

```json
[{
  "a": 45,
  "b": 23
}]
```

The transform "filtered" out all values that are less than 0.

## Examples

The main use case of the `filter` transform is in combination with the `map` transform, when `map` returns too many values.
For example, if looking at browsing history, you might have visited thousands of websites, but only be interested in the ones you visited more than 30 times:

```
map(domain,count) | filter($<=30)
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The script to instantiate to perform on all elements of input, one at a time.</td><td>False</td><td>False</td><td>True</td><td></td></tr></table>
