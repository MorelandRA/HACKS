#!/usr/bin/env python3

"""
TODO:
Refactoring;

Classes for Devices, ( Keyboards, Mice, Other )
Main class
Each keyboard and mouse object gets a listener on construction
Log Mouse Outputs as (X,Y)
Can each device have its own event loop?
"""

from evdev import InputDevice, KeyEvent, RelEvent, SynEvent, categorize, ecodes, list_devices
# evdev docs: https://python-evdev.readthedocs.io/en/latest/index.html
# event codes: https://www.kernel.org/doc/Documentation/input/event-codes.txt

import asyncio

# Find all keyboards automatically
listening = []
others = []

for path in list_devices():
    dev = InputDevice(path)
    caps = dev.capabilities()
    if ecodes.EV_REL or ecodes.EV_KEY in caps:
        listening.append(dev)
    else:
        print(f"Unidentified device with capabilities: {caps}")
        others.append(dev)

print("Listening on:")
for dev in listening:
    print(f" Device: {dev.path} - {dev.name}")


# Async listener for multiple keyboards
async def listen(device):
    async for event in device.async_read_loop():
        event = categorize(event)
        if isinstance(event, KeyEvent):
            print(f" KeyEvent: {device.name}: {event.event.type} - {event.event.code} - {event.keycode}")
        elif isinstance(event, RelEvent):
            print(f" RelEvent: {device.name}: {event.event.type} - {event.event.code} - {event.event.value}")
        elif isinstance(event, SynEvent):
            print(f" SynEvent: {device.name}: {event.event.type} - {event.event.code} - {event.event.value}")
        else:
            print(f" OtherEvent: {device.name}: {event.type} - {event.code} - {event.value}")



# Run all listeners concurrently
loop = asyncio.get_event_loop()
tasks = [listen(dev) for dev in listening]
loop.run_until_complete(asyncio.gather(*tasks))



