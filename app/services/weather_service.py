import os
import aiohttp


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    async def get_weather(self, city: str) -> dict:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('main', {}).get('temp', None)
                else:
                    return None
