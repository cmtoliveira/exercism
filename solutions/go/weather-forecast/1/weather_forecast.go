// Package weather provide tools for weather forecast.
package weather

var (
	// CurrentCondition represents the weather current condition.
    CurrentCondition string
    // CurrentLocation represents the current location.
	CurrentLocation  string
)
// Forecast returns weather forecast given a location and condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
