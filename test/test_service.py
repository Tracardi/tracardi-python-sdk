from tracardi_python_sdk.model.web_page import WebPageResource
from tracardi_python_sdk.model.credentials import Credentials
from tracardi_python_sdk.model.entity import Entity
from tracardi_python_sdk.model.event_payload import EventPayload
from tracardi_python_sdk.model.tracker_payload import TrackerPayload
from tracardi_python_sdk.service.tracardi import Tracardi


def test_send():
    credentials = Credentials(username="admin", password='admin')

    tracardi = Tracardi(url="http://localhost:8686")
    if not tracardi.is_authorized():
        tracardi.authorize(credentials)

    resource = WebPageResource(name="mypage", consent=True)
    resource = tracardi.create_resource(resource)

    payload = TrackerPayload(source=resource, session=Entity(id='87d91e36-0b66-42b5-b9c8-77dc7b224b9a'))
    payload.set_return_profile(True)
    # payload.set_profile('5cb6cd39-3e2b-4e5c-b756-9e167478340e')
    payload.set_context({"my_browser": "ie"})
    payload.add_event(EventPayload(type="event-1", properties={"data": 1}))
    payload.add_event(EventPayload(type="event-2", properties={"data": 2}))
    profile = tracardi.track(payload)
    print(profile)