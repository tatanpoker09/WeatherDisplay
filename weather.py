# import the module
import python_weather

import asyncio
import os


async def getweather(location):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(location)
        return weather
