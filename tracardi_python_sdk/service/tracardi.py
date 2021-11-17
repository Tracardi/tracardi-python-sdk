from typing import Union

from tracardi_python_sdk.errors import AuthenticationError, UnknownError
from tracardi_python_sdk.model.credentials import Credentials
from tracardi_python_sdk.model.entity import Entity
from tracardi_python_sdk.model.profile import Profile
from tracardi_python_sdk.model.resource import Resource
from tracardi_python_sdk.model.token import Token
from tracardi_python_sdk.model.tracker_payload import TrackerPayload
from tracardi_python_sdk.service.sync_dispatcher import SyncDispatcher


class Tracardi:

    def __init__(self, credentials: Credentials, url="http://locahost:8686"):
        self.credentials = credentials
        self.url = url
        self.dispatcher = SyncDispatcher(url)

    def is_authorized(self):
        return self.dispatcher.is_authorized()

    def authorize(self):
        self.dispatcher.authorize(self.credentials)

    def track(self, payload: TrackerPayload) -> Union[Entity, Profile]:
        response = self.dispatcher.send_events(payload)
        data = response.json()

        if 'profile' not in data:
            raise ValueError("Response did not return profile.")

        if payload.options.profile is True:
            return Profile(**data['profile'])
        return Entity(**data['profile'])

    def create_resource(self, resource: Resource) -> Entity:
        response = self.dispatcher.create_resource(resource)
        data = response.json()
        if 'ids' in data and len(data['ids']) == 1:
            return Entity(id=data['ids'][0])
        raise UnknownError("Missing resource is in response.")
