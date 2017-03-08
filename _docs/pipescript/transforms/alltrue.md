<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# alltrue
*Returns true if all datapoints seen have been true*

The `alltrue` transform returns `true` if and only if all of the datapoints seen thus far in the stream have been true:

Given the following data:
```
true,true,true,false,true,true
```

`alltrue` will return:
```
true,true,true,false,false,false
```

### Why It's Useful

Oftentimes you might want to check something in a `while`, or in a `map`. For example,
the following transform will return true for each day where the entire 24 hours was spent at home:

```
distance(<latitude>,<longitude>) < 40 | while(day==next:day,alltrue)
```

The above transform will run a while loop while the current datapoint is part of the same day as the next datapoint, and check whether all location datapoints that day were within 40 meters of your chosen latitude and longitude.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

