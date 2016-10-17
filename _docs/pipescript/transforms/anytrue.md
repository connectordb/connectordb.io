# anytrue
*Returns true if at least one of the datapoints seen was true*

The `anytrue` transform returns `true` if any of the datapoints seen thus far in the stream were true.

Given the following data:
```
false,false,false,true,false,false
```

`anytrue` will return:
```
false,false,false,true,true,true
```

### Why It's Useful

Oftentimes you might want to check something in a `while`, or in a `map`. A great example
would be to check which days you went to the gym:

```
distance(<latitude>,<longitude>) < 40 | while(day==next:day,anytrue)
```

The above transform will run a while loop while the current datapoint is part of the same day as the next datapoint, and check whether any of the GPS coordinates were within 40 meters of your gym.


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

