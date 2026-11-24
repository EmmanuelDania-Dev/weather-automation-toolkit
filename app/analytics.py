def generate_weather_analytics(weather_data: list[dict]) -> dict:

    temperatures = []

    for weather in weather_data:
        temperature = weather["current"]["temperature_2m"]

        temperatures.append(temperature)

    if not temperatures:
        return {}

    average_temperature = round(
        sum(temperatures) / len(temperatures), 2
    )

    hottest_city = max(
        weather_data,
        key=lambda weather: weather["current"]["temperature_2m"]
    )
    coldest_city = min(
        weather_data,
        key=lambda weather: weather["current"]["temperature_2m"]
    )

    humidities = []

    for weather in weather_data:
        humidity = weather["current"]["relative_humidity_2m"]

        humidities.append(humidity)

    average_humidity = round(
        sum(humidities) / len(humidities), 2
    )

    precipitations = []

    for weather in weather_data:
        precipitation = weather["current"]["precipitation"]

        precipitations.append(precipitation)

    total_precipitation = round(sum(precipitations), 2)

    return {
        "average_temperature": average_temperature,
        "hottest_city": hottest_city["city"],
        "hottest_temperature": round(
            hottest_city["current"]["temperature_2m"], 2
        ),
        "coldest_city": coldest_city["city"],
        "coldest_temperature": round(
            coldest_city["current"]["temperature_2m"], 2
        ),
        "average_humidity": average_humidity,
        "total_precipitation": total_precipitation
    }


def display_weather_report(analytics: dict) -> None:

    if not analytics:
        print("No weather data available to generate a report.")
        return

    print("\n========== WEATHER ANALYTICS REPORT ==========")

    print(f"Average Temperature: {analytics['average_temperature']}°C")

    print(
        f"Hottest City: {analytics['hottest_city']} "
        f"({analytics['hottest_temperature']}°C)"
    )

    print(
        f"Coldest City: {analytics['coldest_city']} "
        f"({analytics['coldest_temperature']}°C)"
    )

    print(f"Average Humidity: {analytics['average_humidity']}%")

    print(f"Total Precipitation: {analytics['total_precipitation']} mm")

    print("=" * 40)