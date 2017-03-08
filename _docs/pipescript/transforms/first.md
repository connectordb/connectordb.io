<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# first
*Returns true if first datapoint of a sequence, and false otherwise*

This is true when the datapoint is first in a sequence. It is useful mainly for filtering with if:

```
if first or last
```

will return the first and last datapoint in your stream:

```
1,2,3,4,5
```

```
1,5
```

### Usage
This transform could be finding your wakeup time, based upon the first time you turn on your phone screen in the morning:

```
if dayhour > 4 | while(day == next:day, first) | t
```

The above transform removes the datapoints taken from midnight to 4am (to filter out long nights), and then returns the first datapoint of each day, finaally returning only the timestamp.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td>{"type": "boolean"}</td></tr></table>

