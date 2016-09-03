# REST API

The REST API is split into several parts:


* meta - information about the database, including version, supported transforms, etc.
* websocket - Websocket connection for subscriptions
* crud - create, read, update, delete. This is where you do most housekeeping work, including inserting your data into ConnectorDB
* feed - Atom (RSS) feed for streams
* query - merge and dataset queries (aggregations which use multiple streams of data)


## Authentication

ConnectorDB accepts apikey as a URL parameter, for example:

```
GET /api/v1/crud/myuser?apikey={your_api_key}
```

ConnectorDB also accepts Basic Auth. For user login, standard basic auth is used. When logging in as a device using Basic auth,
the username is empty, and the password is the device API key.

Lastly, the REST API is integrated with the frontend's cookie-based login, so if you are already logged into the web UI,
the REST API will use cookie authentication by default.

## Errors

Everything in the REST API returns the same format of error upon an unsuccessful query. An example error message:

```json
{
	"code": 404,
	"msg": "Can't access this resource",
	"ref":"4289c4f6-c37c-49f3-7dc9-da56c68c8504"
}
```

The code corresponds to the http code, msg is a text message which explains the error, and ref is a reference number for the error.
Errors are logged with their reference number by ConnectorDB, so problems can easily be pinpointed.

----------

<style>
h3 {text-transform: none;color: orange;font-weight: bold;font-size: 150%;}
h4 {color: green;font-weight: bold;}
h5 {color: blue;font-weight: bold;text-transform: none;}
</style>

#### /api/v1

##### GET

###### GET ?q=this

Returns the name of the currently logged in device. If you are not logged in, returns `nobody`

###### GET ?q=countusers

Returns the total number of users in the database. Only database admin has access to this by default

###### GET ?q=countdevices

Returns the total number of devices in the database

###### GET ?q=countstreams

Returns the total number of streams in the database


----------

#### /api/v1/login

##### GET

Uses REST API login methods (url param or Basic auth), and generates a cookie for browser-based login.
This can be used as a backend for manual login

#### /api/v1/logout

##### GET
If there is a user logged in through cookie, deletes the cookie, effectively logging out the user.

----------

#### /api/v1/meta/version

##### GET

Returns the ConnectorDB version

#### /api/v1/meta/transforms

##### GET

Returns the transforms that are supported by this version of ConnectorDB with their documentation

#### /api/v1/meta/interpolators

##### GET

Returns the interpolators that are supported by this version of ConnectorDB with their documentation

----------

#### /api/v1/websocket

You can open a websocket at this location, and subscribe/unsubscribe to live updates of streams.

Each websocket command is of the following format:

```
{
	"cmd": "command",
	"arg": "argument",
	"transform": "optional PipeScript transform for subscribing"
}
```

To subscribe to stream `myuser/mydevice/mystream`, you send:

```json
{
	"cmd": "subscribe",
	"arg": "myuser/mydevice/mystream"
}
```

To unsubscribe, send:

```json
{
	"cmd": "unsubscribe",
	"arg": "myuser/mydevice/mystream"
}
```

When unsubscribing from a stream which used a non-empty transform, the unsubscribe message must include the same exact string for its script.

Once you are subscribed to a stream, whenever you are to receive data, it will come in this format:

```json
{
	"stream": "myuser/mydevice/mystream",
	"transform": "",
	"data": [{"t": 434,"d":"data1"},{"t": 434,"d":"data1"}]
}
```

The transform element is only included if your subscription included a transform.

You can also unsubscribe from all streams:

```json
{
	"cmd": "unsubscribe_all"
}
```

Finally, there is experimental support for inserting datapoints through websocket. As of now, the websocket does not notify of insert success/failure,
so its use is not recommended:

```json
{
	"cmd": "insert",
	"arg": "myuser/mydevice/mystream",
	"d": [{"t": 324324.34,"d": "data"}]
}
```

----------

#### /api/v1/crud/{username}

##### GET

Gets the user. Returns error if user doesn't exist or you have no access to the user.

###### GET ?q=ls

Lists the user's devices


##### POST

Creates the user, with optional streams to create in the user device.

```
POST /api/v1/crud/myuser/
{
	"password": "mypass",
	"email": "my@email",
	"role": "user"
}
```

##### PUT

Allows you to update the user. Set just the fields you want to modify. For example, changing password for user `myuser` would be

```
PUT /api/v1/crud/myuser/
{
	"password": "mypassword"
}
```

##### DELETE

Deletes the user. Returns error if user doesn't exist or not enough permissions.


----------


#### /api/v1/crud/{username}/{devicename}

##### GET

Gets the device. Returns error if it doesn't exist or you have no access.

###### GET ?q=ls

Lists the device's streams

##### POST

Creates the device, with optional streams to create within it.

```
POST /api/v1/crud/myuser/mydevice/
{
	"nickname": "My Awesome Device",
	"role": "none",
	"enabled": true
}
```

##### PUT

Allows you to update the device. Set just the fields you want to modify. See user update (same exact principle).

##### DELETE

Deletes the device. Returns error if it doesn't exist or not enough permissions.


----------

#### /api/v1/crud/{username}/{devicename}/{streamname}

##### GET

Gets the stream. Returns error if it doesn't exist or you have no access.

##### POST

Creates the stream. A schema is required

```
POST /api/v1/crud/myuser/mydevice/mystream
{
	"schema": "{\"type\":\"number\"}"
}
```

##### PUT

Allows you to update the stream. Set just the fields you want to modify. Note that
the JSON Schema is not modifiable.

##### DELETE

Deletes the stream. Returns error if it doesn't exist or not enough permissions.


----------

#### /api/v1/crud/{username}/{devicename}/{streamname}/data

##### GET

Gets the given stream's data. There are two options for getting data.

You can query by timestamps, in which case you
can set t1 and t2 to the desired floating point unix times (with an optional limit in number of datapoints returned)

```
GET /api/v1/crud/myuser/mydevice/mystream/data?t1=3423423.3&t2=44354443&limit=1000
```

You can also query by index (assume that all datapoints in the stream are part of one giant array). Indexing in this
array is python-like, so querying the 10 most recent datapoints can be done by querying i1=-10 and i2=0

```
GET /api/v1/crud/myuser/mydevice/mystream/data?i1=-10&i2=0
```

If you want to query the entire data stream, set i1=0 and i2=0.

Querying also supports PipeScript transforms on the data streams. Simply include the script in the `transform` url param:

```
GET /api/v1/crud/myuser/mydevice/mystream/data?i1=-10&i2=0&transform=if%20last
```

Most libraries will automatically convert spaces and reserved characters to their url equivalents.

###### GET ?q=length

Returns the number of datapoints that the stream contains

###### GET ?q=time2index&t={floating point unix time}

Returns the index in the stream associated with the given timestamp


##### POST

Insert datapoints into the stream. Streams in ConnectorDB are append-only for simplicity. The data is accepted as a JSON array,
with timestamps as floating point unix time.

```
POST /api/v1/crud/myuser/mydevice/mystream/data
[{
	"t": 342342.343,
	"d": "Hello World!"
}]
```

Notice that since ConnectorDB streams are append-only, if a stream attempts to insert data with timestamps which are *older* than
data which already exists in the database, the insert will fail. This brings us to the next version of insert:

##### PUT

This behaves exactly as a POST statement (inserts data into the database), with the major change that it performs restamping of data.
ConnectorDB streams are append-only, and datapoints cannot be inserted with a timestamp lower than timestamps which already exist
in the database.

Since sometimes it does not matter what timestamps data has, but rather the contents of the data itself, this version of insert performs
a "restamp" step to the data, meaning that all datapoints with timestamps lower than data which already exists in the database have their
timestamps rewritten to be the same as the last existing datapoint in the database.



----------

#### /api/v1/feed/{username}/{devicename}/{streamname}

##### GET

Returns the data stream formatted as an Atom feed. Same properties are supported as when querying the stream's data in `GET /api/v1/crud/u/d/s/data`

----------

## Queries

Queries use a bit of shared structure. Each stream within a merge and dataset query is encoded as follows:

```json
{
	"stream": "user/device/stream",
	"transform": "the pipescript transform to un (optional)",
	"i1": 0,
	"i2": 0,
	"t1": 0,
	"t2": 0,
	"limit": 0
}
```

All of these values correspond to the options available when querying a stream for its data. The query only supports either query by index or query by time.

#### /api/v1/query/merge

##### POST

The Merge query is given a list of stream queries to merge (stream queries are shown above):

```
[
{
	"stream": "user1/device1/stream1"
},
{
	"stream": "user2/device2/stream2"
}
]
```

It then returns the two streams merged together into one, and ordered by increasing timestamp.

#### /api/v1/query/dataset

##### POST

The dataset query encodes two query types: both t-datasets and x-datasets.

* T-Datasets

```json
{
	"t1": 342342343,
	"t2": 453423423,
	"dt": 100,
	"dataset": {
		"stream1": {
			"user1/device1/stream1"
			...
		},
		"stream2": {
			"user2/device2/stream2"
			...
		}
	}
}
```

* X-Datasets

```json
{
	"stream": "myuser/mydevice/mystream",
	"i1": -1000,
	"i2": 0,
	"dataset": {
		"stream1": {
			"user1/device1/stream1"
			...
		},
		"stream2": {
			"user2/device2/stream2"
			...
		}
	}
}
```

Each element of the "dataset" part of the query is encoded using the shared "stream" structure. The root stream in x-datasets inherits from the stream structure too,
so anything that works there works with X-Datasets.
