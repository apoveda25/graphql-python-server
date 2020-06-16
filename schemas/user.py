from pydantic import BaseModel, EmailStr, constr, validator
from datetime import datetime as dt
from schemas.helpers.regex import datetime as regex_dt


class UserCreate(BaseModel):
    key: str = None
    email: EmailStr
    active: bool
    username: str
    password: str
    first_name: str = ""
    last_name: str = ""
    image_url: str = ""
    created_at: constr(regex=regex_dt) = dt.now().isoformat()
    created_by: str = ""
    updated_at: constr(regex=regex_dt) = dt.now().isoformat()
    updated_by: str = ""

    @validator("username")
    def lower_username(cls, v):
        return v.lower()

    @validator("first_name")
    def lower_first_name(cls, v):
        return v.lower()

    @validator("last_name")
    def lower_last_name(cls, v):
        return v.lower()

    @validator("password")
    def hash_password(cls, v):
        # Se debe encriptar la contraseña
        return v
