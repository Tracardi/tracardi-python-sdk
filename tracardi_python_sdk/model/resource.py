from typing import Optional

from tracardi_python_sdk.model.entity import Entity


class Resource(Entity):
    type: str
    name: Optional[str] = "No name provided"
    description: Optional[str] = "No description provided"
    config: Optional[dict] = {}
    tags: str = "general"
    enabled: Optional[bool] = True
    consent: bool = False
