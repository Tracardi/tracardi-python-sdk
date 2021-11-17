import aiohttp
from aiohttp import ClientResponse
from tracardi_python_sdk.model.tracker_payload import TrackerPayload
from tracardi_python_sdk.service.dispatcher import Dispatcher


class AsyncDispatcher(Dispatcher):

    async def async_send_events(self, payload: TrackerPayload) -> ClientResponse:
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, data=payload.serialize()) as response:
                body = await response.json()
                if 200 <= response.status < 400:
                    return response
                self._error(body, response.status)

