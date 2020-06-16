from pydantic import BaseModel, EmailStr, constr, validator
from datetime import datetime as dt
from schemas.helpers.regex import datetime as regex_dt


class RolCreate(BaseModel):
    key: str
    name: str
    description: str
    created_at: constr(regex=regex_dt) = dt.now().isoformat()
    created_by: str = ""
    updated_at: constr(regex=regex_dt) = dt.now().isoformat()
    updated_by: str = ""
