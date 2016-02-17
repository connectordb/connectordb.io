---
layout: docsp
---
## Command Line

PipeScript was made to be a standalone language for processing JSON-styled data. While it was originally developed for use in ConnectorDB,
you can easily [embed it](./embedding.html) in your own projects for processing data.

With this in mind, the PipeScript project provides a standalone `pipes` executable, which can read and process data from files or from
the command line. You can download the latest binary here:

<a href="https://github.com/connectordb/pipescript/releases" class="button alt"><i class="fa fa-download"></i> Download</a>

### Usage

Suppose you have a large JSON file, which contains several million datapoints in the following format:

```
[
	{
		"timestamp": "1974-08-11T01:37:45+00:00",
		"something": 5,
		"else": "hi!"
	},
	...
]
```

You can process this file using the pipes executable:

```bash
pipes run "$['something'] | sum | if last" -i mydata.json -ifmt json
```

which will return your processed data in the PipeScript datapoint format.

#### Input Formats

PipeScript supports 3 input formats:

* dp - Datapoint input. This is the internal representation used in PipeScript: `{"t": float64 unix timestamp, "d": the data}`.
* json - A json input, which consists of any json object which includes a timestamp field in RFC3339 format.
* csv - comma separated input, consisting of csv files which include timestamps in RFC3339 format

By default, the `pipes` executable assumes that your input is `dp` formatted. To change the format, use the option `--ifmt=json` or `--ifmt=csv`.

#### Time Stamps

In json and csv mode, timestamps in RFC3339 format are expected. If your dataset does not include timestamps, or the timestamps are irrelevant to
your desired calculation, you can run pipescript without timestamps:

```
pipes run "foo | bar" -i myfile.csv -ifmt csv --notimestamps
```

By default, PipeScript assumes that the first key which can be parsed as a time is the timestamp. To set a custom key, you can use `--timestamp=mykey`.

#### $ in bash

Bash uses the `$` symbol for its own variables. Therefore, when using `pipes` in bash, you will need to escape `$` -> `\$`.
