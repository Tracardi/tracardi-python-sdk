from typing import Optional, Any

from pydantic import BaseModel

from tracardi_python_sdk.model.entity import Entity
from tracardi_python_sdk.model.metadata import Metadata


class ProfileStats(BaseModel):
    visits: int = 0
    views: int = 0
    counters: dict = {}


class ProfileTraits(BaseModel):
    private: Optional[dict] = {}
    public: Optional[dict] = {}


class PII(BaseModel):
    """
    Personally identifiable information, or PII, is any data that could
    potentially be used to identify a particular person. Examples include a full name,
    Social Security number, driver's license number, bank account number,
    passport number, and email address.
    """

    name: Optional[Any] = None
    surname: Optional[Any] = None
    birthDate: Optional[Any] = None
    email: Optional[Any] = None
    telephone: Optional[Any] = None
    twitter: Optional[Any] = None
    facebook: Optional[Any] = None
    whatsapp: Optional[Any] = None
    other: Optional[dict] = {}


class Profile(Entity):
    mergedWith: Optional[str] = None
    metadata: Metadata
    stats: ProfileStats = ProfileStats()
    traits: ProfileTraits = ProfileTraits()
    pii: PII = PII()
    segments: Optional[list] = []
    consents: Optional[dict] = {}
    active: bool = True
