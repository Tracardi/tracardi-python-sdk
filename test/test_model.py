from tracardi_python_sdk.model.entity import Entity
from tracardi_python_sdk.model.event_payload import EventPayload
from tracardi_python_sdk.model.tracker_payload import TrackerPayload


def test_payload():
    payload = TrackerPayload(source=Entity(id="1"))
    assert payload.session is not None

    payload = TrackerPayload(source=Entity(id="1"), session=Entity(id="2"))
    assert payload.session.id == '2'


def test_payload_events():
    payload = TrackerPayload(source=Entity(id="1"))
    event1 = EventPayload(type="event-1", properties={"data": 1})
    payload.add_event(event1)
    payload.add_event(EventPayload(type="event-2", properties={"data": 2}))

    assert len(payload.events) == 2
    for event in payload.events:
        assert isinstance(event, EventPayload)

    assert payload.events[0] == event1


def test_payload_context():
    payload = TrackerPayload(source=Entity(id="1"))
    payload.context = {"browser": "ie"}
    assert payload.context == {"browser": "ie"}
    payload.set_context({"browser": "ie"})
    assert payload.context == {"browser": "ie"}


def test_payload_profile():
    payload = TrackerPayload(source=Entity(id="1"))
    payload.set_profile(profile_id="1")
    assert payload.profile.id == '1'


def test_payload_full():
    payload = TrackerPayload(source=Entity(id="1"), session=Entity(id="2"))
    payload.set_context({"browser": "ie"})
    try:
        payload.serialize()
        assert False
    except ValueError:
        assert True

    payload.add_event(EventPayload(type="event-1", properties={"data": 1}))
    payload.add_event(EventPayload(type="event-2", properties={"data": 2}))
    body = payload.serialize()

    assert body['events'] == [{'type': 'event-1', 'properties': {'data': 1}, 'options': {}},
                              {'type': 'event-2', 'properties': {'data': 2}, 'options': {}}]
    assert body['session']['id'] == '2'
    assert body['source']['id'] == '1'
    assert body['profile'] is None

    payload.set_profile(profile_id='3')

    body = payload.serialize()
    assert body['events'] == [{'type': 'event-1', 'properties': {'data': 1}, 'options': {}},
                              {'type': 'event-2', 'properties': {'data': 2}, 'options': {}}]
    assert body['session']['id'] == '2'
    assert body['source']['id'] == '1'
    assert body['profile']['id'] == '3'
