from locations import locations
from weather import get_weather

def main():
    print("Montana Cast")
    print("-----------------")

    bozeman = locations["Bozeman"]

    print("Getting weather...")

    weather = get_weather(
        bozeman['latitude'],
        bozeman['longitude']
    )

    print(f"Latitude: {bozeman['latitude']}")
    print(f"Longitude: {bozeman['longitude']}")

    print() 
    print("Current Conditions")
    print("-----------------")
    print(f"Temperature: {weather['temperature']}°F")
    print(f"Wind Speed: {weather['wind_speed']}")
    print(f"Precipitation: {weather['precipitation']}in")


if __name__ == "__main__":
    main()