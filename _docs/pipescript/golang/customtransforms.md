# Custom Transforms


This tutorial assumes that you are already familiar with PipeScript, and have gone through [the tutorial](Basics).


To start off, you will need to create a `pipescript.Transform` structure. Before doing anything further, please [look at the documentation](https://godoc.org/github.com/connectordb/pipescript#Transform).

In this tutorial, we will recreate the basic `sum` transform, and test it.

## The sum transform

The sum transform returns the running sum of the datapoints that have been seen thus far in our data stream.

### The initial documentation
Let's start off by creating the general outline of our `pipescript.Transform` object:

```go
var mysum = pipescript.Transform{
	Name: "mysum",
	Description: "Returns the running sum of datapoint values",
	OneToOne: true,	// For each input, we always return an output!
	Stateless: false, // Our result depends on more than just the current datapoint
	Peek: false, // We do not look forward into the sequence - we only need to see current data

	// The OutputSchema is optional, it is the JsonSchema of our output
	OutputSchema: `{"type": "number"}`
}
```

### The transform skeleton

Our transform must conform to the `TransformInstance` interface ([as seen here](https://godoc.org/github.com/connectordb/pipescript#TransformInstance)).

The following skeleton will do that:

```go
type mysumTransform struct {
	CurrentSum float64 // The current sum of datapoints
}

// Copy performs a copy of the current transform with copies of all its internal state
func (t *mysumTransform) Copy() (pipescript.TransformInstance,error) {
	return &mysumTransform{t.CurrentSum},nil
}

// Next is our workhorse function. It is within it that we will implement our transform
func (t *mysumTransform) Next(ti *pipescript.TransformIterator) (*pipescript.Datapoint,error) {
	return nil, errors.New("UNIMPLEMENTED")
}
```

### The Generator

The last thing we need to do before we have a full valid transform is create the generator function, and add it to our Transform object:

```go
var mysum = pipescript.Transform{
	Name: "mysum",
	Description: "Returns the running sum of datapoint values",
	OneToOne: true,	// For each input, we always return an output!
	Stateless: false, // Our result depends on more than just the current datapoint
	Peek: false, // We do not look forward into the sequence - we only need to see current data

	// The OutputSchema is optional, it is the JsonSchema of our output
	OutputSchema: `{"type": "number"}`

	// The Generator function: It is given the Scripts of all the arguments, and returns a TransformInitializer
	Generator: func(name string, args []*pipescript.Script) (*pipescript.TransformInitializer, error) {
		return &pipescript.TransformInitializer{
			Args: args,	// Our transform doesn't use args, but we just pass this through without any changes
			Transform: &mysumTransform{0},	// Initialize our transform with 0
			}, nil
	},
}
```

### The Next function

To fully understand Next, you will need to look at the documentation of [TransformIterator](https://godoc.org/github.com/connectordb/pipescript#TransformIterator) and [TransformEnvironment](https://godoc.org/github.com/connectordb/pipescript#TransformEnvironment)

```go
// Next is our workhorse function. It is within it that we will implement our transform
func (t *mysumTransform) Next(ti *pipescript.TransformIterator) (*pipescript.Datapoint,error) {
	// Get the next TransformEnvironment, which contains our input datapoint
	te := ti.Next()

	if te.IsFinished() {
		// If we get here, then either there was an error, or the iterator finished. We clear our data, so that this transform can be used again
		t.CurrentSum = 0
		return te.Get()	// Since we are at an end condition, we pass through the input
	}

	//Attempt to get our datapoint as a floating point number
	val, err := te.Datapoint.Float()
	if err!=nil {
		return nil,err
	}

	//Update our current sum
	t.CurrentSum += val

	// Return the current sum!
	return te.Set(t.CurrentSum)
}
```


### Registering

Remember we originally created our transform into the variable mysum. In the init function for our module, we have to register this transform, so that the PipeScript parser knows
that it exists.

```go
mysum.Register()
```

## The full transform code:

```go
package mysum

type mysumTransform struct {
	CurrentSum float64 // The current sum of datapoints
}

// Copy performs a copy of the current transform with copies of all its internal state
func (t *mysumTransform) Copy() (pipescript.TransformInstance, error) {
	return &mysumTransform{t.CurrentSum}, nil
}

// Next is our workhorse function. It is within it that we will implement our transform
func (t *mysumTransform) Next(ti *pipescript.TransformIterator) (*pipescript.Datapoint, error) {
	// Get the next TransformEnvironment, which contains our input datapoint
	te := ti.Next()

	if te.IsFinished() {
		// If we get here, then either there was an error, or the iterator finished. We clear our data, so that this transform can be used again
		t.CurrentSum = 0
		return te.Get() // Since we are at an end condition, we pass through the input
	}

	//Attempt to get our datapoint as a floating point number
	val, err := te.Datapoint.Float()
	if err != nil {
		return nil, err
	}

	//Update our current sum
	t.CurrentSum += val

	// Return the current sum!
	return te.Set(t.CurrentSum)
}

var mysum = pipescript.Transform{
	Name:        "mysum",
	Description: "Returns the running sum of datapoint values",
	OneToOne:    true,  // For each input, we always return an output!
	Stateless:   false, // Our result depends on more than just the current datapoint
	Peek:        false, // We do not look forward into the sequence - we only need to see current data

	// The OutputSchema is optional, it is the JsonSchema of our output
	OutputSchema: `{"type": "number"}`,

	// The Generator function: It is given the Scripts of all the arguments, and returns a TransformInitializer
	Generator: func(name string, args []*pipescript.Script) (*pipescript.TransformInitializer, error) {
		return &pipescript.TransformInitializer{
			Args:      args,               // Our transform doesn't use args, but we just pass this through without any changes
			Transform: &mysumTransform{0}, // Initialize our transform with 0
		}, nil
	},
}

func init() {
	mysum.Register()
}

```

And that's it! You have a full working transform!

Of course, this is a very basic transform. To see how more advanced transforms work, you can look at the [transform implementations](https://github.com/connectordb/pipescript/tree/master/transforms/core).


### Testing

What good is code that is not tested? PipeScript includes a special structure that allows you to test your newly created transform. [You can see its docs here](https://godoc.org/github.com/connectordb/pipescript#TestCase).

Create a file called `mysum_test.go` and write the following:

```go
package mysum

import (
	"testing"

	"github.com/connectordb/pipescript"
)

func TestMySum(t *testing.T) {
	// Create a test case
	pipescript.TestCase{
		// The script to run
		Pipescript: "mysum",

		// Our input dataset as a Datapoint array
		Input: []pipescript.Datapoint{
			{1, 1},
			{2, 3},
			{3, 4},
		},
		//Notice that our output is always a float64, since CurrentSum is float64
		Output: []pipescript.Datapoint{
			{1, float64(1)},
			{2, float64(4)},
			{3, float64(8)},
		},

		// SecondaryInput tries putting through an input after the first iterator finishes.
		// this tests our code in the IsFinished() statement and makes sure it cleans stuff up
		SecondaryInput: []pipescript.Datapoint{
			{4, 4},
			{5, 5},
			{6, 6},
		},
		SecondaryOutput: []pipescript.Datapoint{
			{4, float64(4)},
			{5, float64(9)},
			{6, float64(15)},
		},
	}.Run(t) // Run the test case!
}
```

I will leave testing illegal values to you.

<a href="./custominterpolators.html" class="button alt">Custom Interpolators <i class="fa fa-arrow-right"></i></a>
