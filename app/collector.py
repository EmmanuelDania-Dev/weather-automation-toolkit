import asyncio
import httpx
import logging

from app.config import (
    API_BASE_URL,
    REQUEST_TIMEOUT,
    WEATHER_PARAMETERS,
    CITIES,
    MAX_RETRIES
)


async def fetch_weather(city_name: str, coordinates: dict) -> dict:

    url = API_BASE_URL

    params = {
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "current": ",".join(WEATHER_PARAMETERS)
    }

    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:

        for attempt in range(MAX_RETRIES):
            try:

                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                data["city"] = city_name

                return data
            
            except httpx.HTTPError as e:
                logging.warning(
                    f"Weather API request failed on attempt {attempt + 1}: {e}"
                )
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(2)

        raise httpx.HTTPError("Weather API request failed after all retry attempts")


async def fetch_all_weather() -> tuple[list[dict], list[dict]]:

    tasks = []

    for city, details in CITIES.items():
        info = fetch_weather(city, details)

        tasks.append(info)

    results = await asyncio.gather(
    *tasks,
    return_exceptions=True
    )

    successful_data = []
    failed_cities = []

    for city, result in zip(CITIES, results):
        if isinstance(result, Exception):
            failed_cities.append({
                "city": city,
                "error": str(result)
            })
        else:
            successful_data.append(result)

    return successful_data, failed_cities