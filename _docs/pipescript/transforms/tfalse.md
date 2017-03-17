<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# tfalse
*The time period for which a boolean stream is false before turning true*

The time that a stream spends in the `false` state. This transform uses the timestamp, so the timestamp is displayed in the sequence:

```json
[
    {"t": 1, "d": false},
    {"t": 2, "d": false},
    {"t": 4, "d": false},
    {"t": 5, "d": true},
    {"t": 6, "d": true},
    {"t": 7, "d": false},
    {"t": 8, "d": true},
    {"t": 9, "d": false}
]
```

Given the above data, we can get the following:
```
tfalse
```

```json
[
    {"t": 5, "d": 4},
	{"t": 8, "d": 1}
]
```

The stream was `false` from timestamp 1 to 5, when it changed to `true`. So the total time the stream was `false` was 4 seconds.
The stream then turned `false` at timestamp 7, and turned `true` at timestamp 8, meaning that it was `false` for 1 second.
Finally, the stream turned `false` at timestamp 9, but we don't know how long it was `false`, so `tfalse` does not return anything
for this final part.

---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>False</td><td>False</td><td>False</td><td></td><td></td></tr></table>

