from typing import List

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    roles: List[str]
