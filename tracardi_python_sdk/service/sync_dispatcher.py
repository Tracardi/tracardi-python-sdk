import requests as requests
from requests import Response

from tracardi_python_sdk.model.credentials import Credentials
from tracardi_python_sdk.model.resource import Resource
from tracardi_python_sdk.model.token import Token
from tracardi_python_sdk.model.tracker_payload import TrackerPayload
from tracardi_python_sdk.service.async_dispatcher import Dispatcher


class SyncDispatcher(Dispatcher):

    def is_authorized(self) -> bool:
        return self.token != ""

    def _response(self, response):
        body = response.json()
        if 200 <= response.status_code < 400:
            return response
        self._error(body, response.status_code)

    def authorize(self, credentials: Credentials):
        response = requests.post(f"{self.url}/token", data=credentials.dict())
        response = self._response(response)
        self.token = Token(**response.json())

    def send_events(self, payload: TrackerPayload) -> Response:
        response = requests.post(f"{self.url}/track", json=payload.serialize(), headers={"Authorization": f"Bearer {self.token.access_token}"})
        return self._response(response)

    def create_resource(self, resource: Resource):
        response = requests.post(f"{self.url}/resource", json=resource.dict(), headers={"Authorization": f"Bearer {self.token.access_token}"})
        return self._response(response)
