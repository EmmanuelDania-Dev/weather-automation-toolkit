
import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock

from app.collector import fetch_weather, fetch_all_weather


def create_mock_response():
    response = MagicMock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "current": {
            "temperature_2m": 30,
            "relative_humidity_2m": 70,
            "apparent_temperature": 32,
            "precipitation": 0.0,
            "wind_speed_10m": 12
        }
    }

    return response


@pytest.mark.asyncio
async def test_fetch_weather_success(monkeypatch):
    mock_response = create_mock_response()
    mock_get = AsyncMock(return_value=mock_response)

    monkeypatch.setattr(
        "app.collector.httpx.AsyncClient.get",
        mock_get
    )

    result = await fetch_weather(
        "Lagos",
        {"latitude": 6.5244, "longitude": 3.3792}
    )

    assert result["city"] == "Lagos"
    assert result["current"]["temperature_2m"] == 30
    mock_get.assert_awaited_once()


@pytest.mark.asyncio
async def test_fetch_weather_retry_success(monkeypatch):
    mock_response = create_mock_response()

    mock_get = AsyncMock(
        side_effect=[
            httpx.ConnectError("Connection failed"),
            mock_response
        ]
    )

    mock_sleep = AsyncMock()

    monkeypatch.setattr(
        "app.collector.httpx.AsyncClient.get",
        mock_get
    )
    monkeypatch.setattr(
        "app.collector.asyncio.sleep",
        mock_sleep
    )

    result = await fetch_weather(
        "Lagos",
        {"latitude": 6.5244, "longitude": 3.3792}
    )

    assert result["city"] == "Lagos"
    assert mock_get.await_count == 2
    mock_sleep.assert_awaited_once()


@pytest.mark.asyncio
async def test_fetch_weather_all_retries_fail(monkeypatch):
    mock_get = AsyncMock(
        side_effect=httpx.ConnectError("Connection failed")
    )
    mock_sleep = AsyncMock()

    monkeypatch.setattr(
        "app.collector.httpx.AsyncClient.get",
        mock_get
    )
    monkeypatch.setattr(
        "app.collector.asyncio.sleep",
        mock_sleep
    )

    with pytest.raises(
        httpx.HTTPError,
        match="Weather API request failed after all retry attempts"
    ):
        await fetch_weather(
            "Lagos",
            {"latitude": 6.5244, "longitude": 3.3792}
        )

    assert mock_get.await_count == 3
    assert mock_sleep.await_count == 2


@pytest.mark.asyncio
async def test_fetch_all_weather_partial_failure(monkeypatch):

    async def mock_fetch_weather(city, coordinates):
        if city == "London":
            raise httpx.HTTPError("Simulated failure")

        return {"city": city}

    monkeypatch.setattr(
        "app.collector.fetch_weather",
        mock_fetch_weather
    )

    successful_data, failed_cities = await fetch_all_weather()

    assert len(successful_data) == 4
    assert len(failed_cities) == 1
    assert failed_cities[0]["city"] == "London"
