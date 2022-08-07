"""SBot Servo Board Test Script."""
from time import sleep

from sbot import Robot


def test_servo(r: Robot):
    """Test the servo board."""
    print(f"Name: {r.servo_board.name}")
    print(f"Serial: {r.servo_board.serial_number}")
    print(f"FW: {r.servo_board.firmware_version}")

    for s in r.servo_board.servos:

        for p in [0, 1, -1, 0]:
            print(f"Setting servo {s.identifier} to {p}")
            s.position = p
            sleep(0.5)
