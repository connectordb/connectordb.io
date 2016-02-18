---
layout: docs
---
## How it Works

ConnectorDB is built with the totally connected person in mind. It is meant to be a centralized repository for your internet connected devices' and sensors' gathered data,
as well as your personal insights and ratings. By having such details in one place, it is possible to perform some very interesting analysis!

### Streams

Streams are the lowest level units in ConnectorDB. Every sensor you have access to can be considered a stream. For example, a temperature sensor which reports the temperature in your house every 15 seconds would be considered a stream.
In ConnectorDB, it is best to divide streams into the smallest independent components. A stream should have little to no structure. The temperature sensor would have each datapoint in its stream
be a single number - the current temperature. Such simplicity makes data analysis easy.

### Devices

Devices are collections of streams. A great example of a device would be your phone. Your smartphone gathers data about you into its streams, such as gathering your step count into the "steps" stream.
Devices are also the access level of ConnectorDB. That is, devices can directly log into the database to perform operations on it. Each device is associated with an API key, with which it can log in to synchronize
data.

### Users

A user in ConnectorDB is a collection of devices. Users access the database through a special "user" device (since access in ConnectorDB is through devices). The user device is a centralized repository for manually
entered data, such as ratings, logs, etc. Anything that is not gathered automatically through an external device belongs in the "user" device.

----------

### Gathering Data

It is expected that you will gather detailed data from many sources into ConnectorDB, which will serve as a centralized repository. This will allow plugin Machine Learning algorithms to perform optimizations
based upon your data - imagine a smart home which heats up your house when you are driving home from work, due to monitoring your phone's location data.

Or perhaps imagine a music streaming service which changes music types based on your heart rate, stress level, your schedule, and a variety of other pieces of data gathered by ConnectorDB.

ConnectorDB itself does not include ML, as it is focused on being a general purpose data-gathering platform. However, it is built with integration into larger learning systems in mind.
