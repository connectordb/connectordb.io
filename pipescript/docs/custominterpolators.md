---
layout: docsp
---
## Custom Interpolators

It is assumed that you have already followed the [custom transform tutorial](./customtransforms.html).

Interpolators are simpler than transforms, since they do not have any arguments or complex environments. We will implement the `sum` interpolator.

Interpolators are given "interpolation timestamps", which are timestamps which represent the location in time at which to "interpolate".

The sum interpolator sums up the data from the datapoints in its stream in between two points. That is, if two interpolation points are 2.71 and 3.14,
the sum interpolator for 3.14 returns the sum of all datapoints from 2.71 exclusive all the way to 3.14 inclusive.

```go
package mysum
import (
	"github.com/connectordb/pipescript"
	"github.com/connectordb/pipescript/interpolator"
)

// MySumInterpolator sums the data in each interpolation time period
type MySumInterpolator struct {
	// The data stream underlying the interpolator
	Iterator pipescript.DatapointIterator
	// A cache of one datapoint
	dp       *pipescript.Datapoint
}

// Interpolate performs the interpolation. It is given the "Interpolation time" as
// an argument.
func (i *SumInterpolator) Interpolate(ts float64) (*pipescript.Datapoint, error) {
	sum := float64(0)

	// While the datapoint's timestamp is less than the "interpolation time"
	for i.dp != nil && i.dp.Timestamp <= ts {
		d, err := i.dp.Float()
		if err != nil {
			return nil, err
		}
		// Add to the sum
		sum += d

		i.dp, err = i.Iterator.Next()
		if err != nil {
			return nil, err
		}
	}

	return &pipescript.Datapoint{ts, sum}, nil
}

var MySum = interpolator.Interpolator{
	Name:        "mysum",
	Description: "Returns the sum of datapoints in its interpolation time.",
	Generator: func(name string, dpi pipescript.DatapointIterator) (i interpolator.InterpolatorInstance, err error) {
		dp, err := dpi.Next()
		return &SumInterpolator{dpi, dp}, err
	},
}

```

Remember that your interpolator must be registered before it can be used!

### Testing

Just like with Transforms, Interpolators also include their own special [testing structure](https://godoc.org/github.com/connectordb/pipescript/interpolator#TestCase):

```go
package mysum

import (
	"testing"

	"github.com/connectordb/pipescript"
	"github.com/connectordb/pipescript/interpolator"
)


// The standard datapoint array to use when testing
var testDpa = []pipescript.Datapoint{
	{1., 10},
	{2., 20},
	{3., 30},
	{4., 40},
	{5., 50},
	{6., 60},
	{6., 70},
	{7., 80},
	{8., 90},
}

func TestMySum(t *testing.T) {
	MySum.Register()
	interpolator.TestCase{
		Interpolator: "mysum",
		Input:        testDpa,

		Output: []interpolator.TestOutput{
			{0.5, &pipescript.Datapoint{0.5, 0.0}},
			{2.5, &pipescript.Datapoint{2.5, float64(30)}},
			{5.0, &pipescript.Datapoint{5, float64(120)}},
			{6.0, &pipescript.Datapoint{6, float64(130)}},
			{8.0, &pipescript.Datapoint{8, float64(170)}},
			{20.0, &pipescript.Datapoint{20, 0.0}},
			{30.0, &pipescript.Datapoint{30, 0.0}},
		},
	}.Run(t)
}

```
