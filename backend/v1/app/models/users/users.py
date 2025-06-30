from typing import Optional
import string
from datetime import datetime

from pydantic import EmailStr, constr, validator, HttpUrl

from backend.v1.app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin


def validate_username(username: str) -> str:
    allowed = string.ascii_letters + string.digits + "-" + "_"
    assert all(char in allowed for char in username), "Invalid characters in username."
    assert len(username) >= 3, "Username must be 3 characters or more."
    return username


class UserBase(CoreModel):
    """
    All common characteristics of our users
    """
    first_name: str
    last_name: str
    email: EmailStr
    email_verified: bool = False
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    "attributes required to create a new resource - used at POST requests"
    password: constr(min_length=7, max_length=100)
    username: constr(min_length=3, max_length=20)

    # @validator("username", pre=True)
    def username_is_valid(cls, username: str) -> str:
        return validate_username(username)