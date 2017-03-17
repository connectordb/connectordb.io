<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# dt
*Returns time difference between this and previous datapoint*

The `dt` transform allows you to quickly find the time difference between the previous and this datapoint:

```json
[
    {"t": 4, "d": 4},
	{"t": 20, "d": 5},
	{"t": 50, "d": 6}
]
```

```
dt
```

```json
[
    {"t": 4, 0)},
	{"t": 20, "d": 16},
	{"t": 50, "d":30}
]
```

---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

