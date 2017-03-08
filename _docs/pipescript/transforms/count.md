<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# count
*Counts the number of datapoints that have been seen. It is equivalent to the i in a loop over the sequence.*

Count represents the total number of datapoints passed through the transform. It is equivalent to an `i` used in a loop over an array, with the difference that count starts from 1, rather than 0.

No matter what the datapoints, the sequence of data that count returns is:

```
1,2,3,4,5...
```

### Usage

#### Counting Mood
Suppose you want to count the number of times you were in a great mood:
```
if $ >= 8 | count | if last
```

The above transform will return only the datapoints where your mood rating was 8 or above, it will count them, and only return the last datapoint (which contains the full count).

#### Counting Visits
Suppose you want to find how many times you visited a friend:

```
if distance(<latitude>,<longitude>) < 50 | if changed | if $ | count | if last
```

The above transform finds when you were within 50 meters of the given coordinates (your friend's home), filters these datapoints so only changes remain (so each time you visit, you get one `true`, followed by a `false` when you leave), filter the false values, and count the number of times you visited. Note that `if $ | count` can be replaced with `sum` in this case.

#### Counting Weekdays
Now you want to see which weekdays you use your computer the most. You can simply count the datapoints in your laptop's stream to see what days have most data:

```
map(weekday,count)
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td>{"type": "integer","minimum": 0}</td></tr></table>

