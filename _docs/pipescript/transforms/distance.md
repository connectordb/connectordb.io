# distance
*Returns distance in meters from given latitude/longitude coordinates to datapoint*

The `distance` transform computes the distance in meters from the current datapoint to its argument coordinates.

The datapoint is assumed to have `latitude` and `longitude` fields in decimal coordinates. It returns the distance in meters computed using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula).

```json
[{
  "latitude": 40.4277304,
  "longitude": -86.9170587
}]
```
Given the above stream, we find its distance to the chosen coordinate: `distance(40.426841,-86.9165106)`:
```json
[109.238]
```

The two coordinates above are about 109 meters apart.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td>{"type": "boolean"}</td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>Latitude</td><td>False</td><td>True</td><td>False</td><td></td></tr><tr><td>2</td><td>Longitude</td><td>False</td><td>True</td><td>False</td><td></td></tr></table>
