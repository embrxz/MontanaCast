import requests

def get_water_data(station_id):
    url = "https://waterservices.usgs.gov/nwis/iv/"

    parameters = {
        "format": "json", "sites": station_id, "parameterCd": "00060,00010,00065"

    }

    try:
        response = requests.get(
        url,
        params=parameters,
        timeout=10
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        print(f"Unable to retrieve USGS river data: {error}")
        return {}

    data = response.json()

    time_series = data["value"]["timeSeries"]

    water_data = {}

    for series in time_series:

        parameter_code = series["variable"]["variableCode"][0]["value"]

        values = series["values"][0]["value"]

        if len(values) == 0:
            continue

        current_value = values[-1]["value"]

        if parameter_code == "00060":
            water_data["streamflow"] = float(current_value)

        elif parameter_code == "00065":
            water_data["gauge_height"] = float(current_value)

        elif parameter_code == "00010":
            temperature_c = float(current_value)
            temperature_f = (temperature_c * 9 / 5) + 32

            water_data["water_temperature"] = round(temperature_f, 1)     
            
    return water_data