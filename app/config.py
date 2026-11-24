APP_NAME = "Weather Automation Toolkit"

API_BASE_URL = "https://api.open-meteo.com/v1/forecast"

REQUEST_TIMEOUT = 10

MAX_RETRIES = 3

CITIES = {
    "Lagos": {
        "latitude": 6.5244,
        "longitude": 3.3792
    },
    "London": {
        "latitude": 51.5072,
        "longitude": -0.1276
    },
    "New York": {
        "latitude": 40.7128,
        "longitude": -74.0060
    },
    "Tokyo": {
        "latitude": 35.6762,
        "longitude": 139.6503
    },
    "Nairobi": {
        "latitude": -1.2921,
        "longitude": 36.8219
    }
}

WEATHER_PARAMETERS = [
    "temperature_2m",
    "relative_humidity_2m",
    "apparent_temperature",
    "precipitation",
    "wind_speed_10m"
]
