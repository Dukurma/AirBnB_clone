#!/usr/bin/env python3
"""Create the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
