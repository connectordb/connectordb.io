
Transforms: PipeScript
=======================================

ConnectorDB uses a tiny  time-series analysis language, called PipeScript, to transform your data into desired format.

The goal of PipeScript is to make most data preparation a single line of code.

* [Try It Online](transforms/index.md)
* [Tutorial](tutorial/basics.md)
* [Extending PipeScript](golang/index.rst)

Every query for data in ConnectorDB supports transforms. This means that you can have ConnectorDB pre-compute many statistics about your data.

For example, `sum | if last` will compute the running sum of the datapoints, and return only the last datapoint, giving you a sum of all datapoints' data. For an in-depth tutorial of PipeScript,
please follow the tutorial link above.

