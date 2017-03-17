<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# ttrue
*The time period for which a boolean stream is true before turning false*

The time that a stream spends in the `true` state. This transform uses the timestamp, so the timestamp is displayed in the sequence:

```json
[
    {"t": 1, "d": true},
    {"t": 2, "d": true},
    {"t": 4, "d": true},
    {"t": 5, "d": false},
    {"t": 6, "d": false},
    {"t": 7, "d": true},
    {"t": 8, "d": false},
    {"t": 9, "d": true}
]
```

Given the above data, we can get the following:
```
ttrue
```

```json
[
    {"t": 5, "d": 4},
	{"t": 8, "d": 1}
]
```

The stream was `true` from timestamp 1 to 5, when it changed to `false`. So the total time the stream was `true` was 4 seconds.
The stream then turned `true` at timestamp 7, and turned `false` at timestamp 8, meaning that it was `true` for 1 second.
Finally, the stream turned `true` at timestamp 9, but we don't know how long it was `true`, so `ttrue` does not return anything
for this final part.

---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>False</td><td>False</td><td>False</td><td></td><td></td></tr></table>

