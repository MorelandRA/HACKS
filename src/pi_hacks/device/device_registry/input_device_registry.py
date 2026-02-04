from ..input_device.input_device import InputDevice

from evdev import list_devices


class InputDeviceRegistry:
    def __init__(self):
        print("Creating a device registry from ", list_devices())
        self._devices = [InputDevice(path) for path in list_devices()]
        for device in self._devices:
            device.open_listener()

    def get_input_devices(self):
        return self._devices





