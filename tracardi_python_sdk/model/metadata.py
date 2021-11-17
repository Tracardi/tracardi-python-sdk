from pydantic import BaseModel
from tracardi_python_sdk.model.time import Time


class Metadata(BaseModel):
    time: Time
    ip: str = None
