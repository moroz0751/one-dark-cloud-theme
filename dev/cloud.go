package main

import (
	"fmt"
	"math/rand"
	"time"
)

var CloudTypes = [4]string{"Cumulus", "Stratus", "Cirrus", "Nimbostratus"}

type Climber interface {
	climb(increase int) int
}

// One dark but not so stormy night...
type Cloud struct {
	Color     string
	Type      string
	Timestamp time.Time
	Altitude  int
}

func (c *Cloud) Climb(increase int) int {
	c.Altitude += increase
	return c.Altitude
}

func randType() string {
	i := rand.Intn(len(CloudTypes))
	return CloudTypes[i]
}

func genAltitude() int {
	const min int = 100
	const max int = 1000
	return rand.Intn(max-min) + min
}

func main() {
	myCloud := Cloud{
		Color:     "gray",
		Type:      randType(),
		Timestamp: time.Now().UTC(),
		Altitude:  genAltitude(),
	}
	myCloud.Climb(250)
	fmt.Printf("New cloud: %v\n", myCloud)
}
