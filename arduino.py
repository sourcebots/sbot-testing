"""SBot Arduino Test Script."""
from time import sleep

from sbot import Robot, AnaloguePin, GPIOPinMode


def test_arduino(r: Robot):
    """Test the arduino."""
    print(f"Name: {r.arduino.name}")
    print(f"Serial: {r.arduino.serial}")
    print(f"FW: {r.arduino.firmware_version}")

    for i in range(2, 14):
        print(f"Testing digital pin {i}")
        p = r.arduino.pins[i]

        print("Setting mode to DIGITAL_OUTPUT")
        p.mode = GPIOPinMode.DIGITAL_OUTPUT
        print("Set pin High")
        p.digital_state = True
        sleep(0.5)
        print("Set pin False")
        p.digital_state = False
        sleep(0.5)

        print("Setting mode to DIGITAL_INPUT")
        p.mode = GPIOPinMode.DIGITAL_INPUT
        print(f"State: {p.digital_state}")

        sleep(0.5)

        print("Setting mode to DIGITAL_INPUT_PULLUP")
        p.mode = GPIOPinMode.DIGITAL_INPUT_PULLUP
        print(f"State: {p.digital_state}")

    for i in [AnaloguePin.A0, AnaloguePin.A1, AnaloguePin.A2, AnaloguePin.A3]:
        print(f"Testing analogue pin {i}")
        p = r.arduino.pins[i]

        print("Setting mode to ANALOGUE_INPUT")
        p.mode = GPIOPinMode.ANALOGUE_INPUT

        print(f"State: {p.analogue_value}")

    u = r.arduino.ultrasound_sensors[11, 10]

    for _ in range(0, 10):

        print(f"Pulse: {u.pulse()}")
        print(f"Distance: {u.distance()}")
