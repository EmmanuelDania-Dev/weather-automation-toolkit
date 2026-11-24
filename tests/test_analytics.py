from app.analytics import (
    generate_weather_analytics,
    display_weather_report
)


weather_data = [
    {
        "city": "Lagos",
        "current": {
            "temperature_2m": 30,
            "relative_humidity_2m": 70,
            "precipitation": 0.5
        }
    },
    {
        "city": "London",
        "current": {
            "temperature_2m": 10,
            "relative_humidity_2m": 80,
            "precipitation": 1.5
        }
    },
    {
        "city": "Tokyo",
        "current": {
            "temperature_2m": 20,
            "relative_humidity_2m": 60,
            "precipitation": 1.0
        }
    }
]


def test_average_temperature():
    result = generate_weather_analytics(weather_data)

    assert result["average_temperature"] == 20


def test_hottest_city():
    result = generate_weather_analytics(weather_data)

    assert result["hottest_city"] == "Lagos"
    assert result["hottest_temperature"] == 30


def test_coldest_city():
    result = generate_weather_analytics(weather_data)

    assert result["coldest_city"] == "London"
    assert result["coldest_temperature"] == 10

def test_average_humidity():
    result = generate_weather_analytics(weather_data)

    assert result["average_humidity"] == 70

def test_total_precipitation():
    result = generate_weather_analytics(weather_data)

    assert result["total_precipitation"] == 3.0

def test_empty_weather_data():
    result = generate_weather_analytics([])

    assert result == {}

def test_empty_weather_report(capsys):
    display_weather_report({})

    captured = capsys.readouterr()

    assert "No weather data available" in captured.out

def test_weather_report(capsys):
    analytics = generate_weather_analytics(weather_data)

    display_weather_report(analytics)

    captured = capsys.readouterr()

    assert "Average Temperature: 20.0°C" in captured.out
    assert "Hottest City: Lagos (30°C)" in captured.out
    assert "Coldest City: London (10°C)" in captured.out
    assert "Average Humidity: 70.0%" in captured.out
    assert "Total Precipitation: 3.0 mm" in captured.out