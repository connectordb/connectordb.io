---
layout: docsp
---
## Datasets

**NOTE:** *The Dataset API is still undergoing heavy development, and as such might change quite a bit in the near future.
In particular, the Dataset API is not yet completely moved to PipeScript, and as such is only readily accessible through ConnectorDB.*

Datasets are one of the most powerful features of PipeScript. The underlying issue is simple: You have multiple sensors gathering data
at the same time. Each sensor is independent, so they do not have synchronized timestamps.


| Timestamp | Mood Rating  |   | Timestamp | Room Temperature (F) |
|-----------|--------------|---|-----------|----------------------|
| 1pm       | 7            |   | 2pm       | 73                   |
| 4pm       | 3            |   | 5pm       | 84                   |
| 11pm      | 5            |   | 8pm       | 81                   |
|           |              |   | 11pm      | 79                   |
