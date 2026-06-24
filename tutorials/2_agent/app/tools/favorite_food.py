"""Favorite food tool used by the tutorial agent."""

from langchain.tools import tool
from pydantic import BaseModel, Field


class FavoriteFoodInput(BaseModel):
    animal: str = Field(
        description="The animal for which we want the favorite food."
    )


@tool(args_schema=FavoriteFoodInput)
def get_favorite_food(animal: str) -> str:
    """Use this tool when the user asks what food a given animal likes."""
    fake_foods = {
        "cat": "salmon",
        "dog": "chicken",
        "rabbit": "carrots",
    }
    return fake_foods.get(
        animal.lower(), f"I do not know the favorite food of {animal}."
    )
