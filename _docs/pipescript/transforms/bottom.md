<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# bottom
*Takes a json object, and returns the bottom n elements*

The `bottom` transform is an equivalent of the `top` transform, 
but it returns the bottom-most elements. See the `top` transform for further documentation.

---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The number of elements to retain of the object</td><td>False</td><td>False</td><td>False</td><td></td></tr><tr><td>2</td><td>The script to run ($ default) to generate weights over which to sort</td><td>True</td><td>False</td><td>True</td><td>None</td></tr></table>
