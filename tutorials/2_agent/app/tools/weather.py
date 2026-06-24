"""Weather tool used by the tutorial agent."""

from langchain.tools import tool
from pydantic import BaseModel, Field


class WeatherInput(BaseModel):
    city: str = Field(description="The city for which we want the weather. Put only the city in lower case and do not add the country")


@tool(args_schema=WeatherInput)
def get_weather(city: str) -> str:
    """Use this tool when the user asks for the weather in a city."""
    fake_weather = {
        "brussels": "Cloudy, 18C",
        "paris": "Sunny, 24C",
        "london": "Rainy, 16C",
    }
    return fake_weather.get(city.lower(), f"No fake weather data found for {city}.")
