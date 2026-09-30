from locations import locations
from weather import get_weather
from water import get_water_data

def main():
    print("Montana Cast")
    print("-----------------")

    location = locations["Gallatin River - Big Sky"]

    print("Getting weather...")

    weather = get_weather(
        location['latitude'],
        location['longitude']
    )

   

    print() 
    print("Current Conditions")
    print("-----------------")
    print(f"Temperature: {weather['temperature']}°F")
    print(f"Wind Speed: {weather['wind_speed']}")
    print(f"Precipitation: {weather['precipitation']}in")


    print()
    print("Getting river data...")

    water = get_water_data(
        location["usgs_station"]
    )

    print()
    print("River Conditions")
    print("--------------------")

    if "streamflow" in water:
        print(f"Streamflow: {water['streamflow']} CFS")

    if "gauge_height" in water:
        print(f"Gauge Height: {water['gauge_height']} ft")

    if "water_temperature" in water:
        print(f"Water Temperature: {water['water_temperature']}°F")

if __name__ == "__main__":
    main()