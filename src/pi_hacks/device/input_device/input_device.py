from asyncio import create_task
from evdev import InputDevice as EvdevDevice


class InputDevice:

    def __init__(self, device):
        self._device = EvdevDevice(device)
        self._task = create_task(self._listen(self._device))
        self._enabled = False
        print(f"Created device: {self._device.name}")

    def open_listener(self):
        self._enabled = True

    def close_listener(self):
        self._enabled = False

    async def _listen(self, device):
        async for event in device.async_read_loop():
            if self._enabled:
                print(f"Received type {event.type} event from {device.name} at second [{event.sec}.{event.usec}]"
                      f"  Code: {event.code}, Value: {event.value}")

    def get_task(self):
        return self._task

