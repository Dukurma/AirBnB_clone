#!/usr/bin/python3
"""Create the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): City's name.
    """

    state_id = ""
    name = ""
