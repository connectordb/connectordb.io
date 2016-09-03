## Embedding PipeScript

So you want to embed PipeScript in your project. This page will show you what you need to do!

It is assumed that you have already gone over and understand [the tutorial](basics.html).

### Preparation

In order to get PipeScript working with your database or project, you need to do two things: Fit your data into a `pipescript.Datapoint`, and implement a `DatapointIterator`

### Datapoint

This is the workhorse of PipeScript:

```go
type Datapoint struct {
	Timestamp float64 `json:"t"`  // The UNIX timestamp in seconds
	Data interface{}  `json:"d"`  // The Data associated with the datapoint
}
```

Whatever your data format is, you will need to somehow fit it into the `pipescript.Datapoint` structure. If you have tabular data, `map[string]interface{}` is recommended for the Data portion of your Datapoints.

For more information, look at [Datapoint's documentation](https://godoc.org/github.com/connectordb/pipescript#Datapoint)

### DatapointIterator


The core underlying interface in use with PipeScript is the DatapointIterator

```go
type DatapointIterator interface {
	Next() (*pipescript.Datapoint,error)
}
```

The iterator is what is used as an input to PipeScript, and it is what a parsed script returns. This allows parsing through gigabytes of data, since only a small fraction of the total dataset is being processed at one time.

The DatapointIterator returns your datapoint and nil error while it has data. Once it runs out of data, it returns nil,nil, which signifies an EOF. If at any point in time Next() returns an error, the iterator is assumed dead, and the entire pipeline using the iterator is no longer usable.

For more detail on DatapointIterator, [look at its documentation](https://godoc.org/github.com/connectordb/pipescript#DatapointIterator).


## Getting things working

```go
package main

import (
	"fmt"

	"github.com/connectordb/pipescript" // Imports pipescript

	"log"

	"github.com/connectordb/pipescript/transforms"
)

// Replace this with your own implementation of DatapointIterator
type MyDatapointIterator struct {
	MyData       []int
	MyTimestamps []float64
	iter         int
}

// Next is the only method you need to implement
func (myiter *MyDatapointIterator) Next() (*pipescript.Datapoint, error) {
	i := myiter.iter
	if i >= len(myiter.MyData) {
		return nil, nil // When done, return nil,nil
	}
	dp := &pipescript.Datapoint{Timestamp: myiter.MyTimestamps[i], Data: myiter.MyData[i]}

	myiter.iter++
	return dp, nil
}

func main() {
	// Registers all of the transforms that come with PipeScript (the PipeScript 'standard library').
	// you can pick and choose the transforms you want by importing only the sub-directories you want.
	// Look at https://github.com/connectordb/pipescript/tree/master/transforms for details
	transforms.Register()

	fmt.Printf("Running My Script!\n")

	// The Parse method will generate your script
	s, err := pipescript.Parse("if $ < 5 | sum")
	if err != nil {
		log.Fatal(err.Error())
	}

	// SetInput sets the input iterator of PipeScript
	s.SetInput(&MyDatapointIterator{
		[]int{3, 7, 2, 4},
		[]float64{1, 2, 3, 4},
		0,
	})

	dp := &pipescript.Datapoint{}
	for dp != nil && err == nil {
		// Get the next output datapoint from the script
		dp, err = s.Next()

		fmt.Printf("%v\n", dp)
	}
	if err != nil {
		log.Fatal(err.Error())
	}

	fmt.Printf("Done!\n")
}
```


<a href="./customtransforms.html" class="button alt">Custom Transforms <i class="fa fa-arrow-right"></i></a>
