<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->

# reduce
*Takes a json object, and considers each field to be a separate datapoint's data.
It then hijacks its argument, and performs the given transform on all of the fields, returning the result.*

`reduce` performs a given transform on all the elements of a multi-element datapoint.

Suppose you have the following data:
```json
[
  {
    "a": 3,
    "b": 5
  },
  {
    "q": 10,
    "z": 23
  }
]
```

Then the transform `reduce(sum)` will give you:

```json
[8,33]
```

Reduce took each element in the given datapoint, and applied the transform `sum` to it.

## Usage

The reduce transform is particularly useful in conjunction with the `map` transform.

Suppose you want to find the average number of steps taken every weekday.

Running the following transform will give you a map of weekday to average step count:

```
while(day==next:day,sum) | map(weekday, mean)
```

For example, a possible result of the above transform could be:
```json
[
{
  "Monday": 12243,
  "Tuesday": 13452,
  "Wednesday": 14523,
  "Thursday": 9543,
  "Friday": 20487,
  "Saturday": 3000,
  "Sunday": 4000
}
]
```

You can now find the average per weekday by running `reduce(mean)`, giving a final transform:

```
while(day==next:day,sum) | map(weekday, mean) | reduce(mean)
```


---

#### Transform Details
<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead><tr><td>True</td><td>False</td><td>False</td><td></td><td></td></tr></table>

### Arguments
<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead><tr><td>1</td><td>The script to instantiate to perform on all elements of input</td><td>False</td><td>False</td><td>True</td><td></td></tr></table>
