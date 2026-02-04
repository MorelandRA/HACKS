#!/usr/bin/env python3
from device.device_registry.input_device_registry import InputDeviceRegistry

"""
TODO:
Refactoring;
Log Mouse Outputs as (X,Y)
Tests
"""

# evdev docs: https://python-evdev.readthedocs.io/en/latest/index.html
# event codes: https://www.kernel.org/doc/Documentation/input/event-codes.txt

import asyncio

async def main():
    device_registry = InputDeviceRegistry()
    for device in device_registry.get_input_devices():
        device.open_listener()
    await asyncio.Event().wait()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())



