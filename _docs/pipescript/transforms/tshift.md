# tshift
*Shift the datapoint timestamp by a constant number of seconds*

This transform is not particularly useful for PipeScript by itself, but becomes very frequently used in dataset and merge queries.

Every datapoint has a data portion, as well as a timestamp, which is hidden from computations in PipeScript by default. `tshift` shifts the timestamps of a stream by the given amount in seconds. This allows making it seem like the data of a stream came before/after its actual timestamps. This is useful in datasets, since a tshift can allow interpolating between different time ranges - it allows asking questions such as "does exercise today impact my mood a week later?". The datapoints corresponding to mood can be tshifted back by a week to correspond directly to the original datapoints where your exercise data is shown.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>True</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The number of seconds to shift the timestamp</td><td>False</td><td>True</td><td>False</td><td></td></tr></table>
