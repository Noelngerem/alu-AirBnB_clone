#!/usr/bin/python3
"""
This file inherits from BaseModel
and defines the UserModel class
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User Model"""

    # Class attributes with type annotations
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
