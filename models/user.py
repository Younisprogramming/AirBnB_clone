#!/usr/bin/python3
"""this is my class doc """
from models.base_model import BaseModel


class User(BaseModel):
    """ my users """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
