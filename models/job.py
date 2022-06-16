import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class Job(BaseModel):
    id: Optional[str] = None
    user_id: int
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime