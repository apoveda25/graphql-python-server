from pydantic import BaseModel, EmailStr, constr, validator
from enum import Enum
from datetime import datetime as dt
from schemas.helpers.regex import datetime as regex_dt


class Action(str, Enum):
    READ = "READ"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class ScopeCreate(BaseModel):
    key: str = None
    name: str = ""
    description: str
    action: Action
    collection: str
    created_at: constr(regex=regex_dt) = dt.now().isoformat()
    created_by: str = ""
    updated_at: constr(regex=regex_dt) = dt.now().isoformat()
    updated_by: str = ""
