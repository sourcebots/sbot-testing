"""SBot Motor Board Test Script."""
from math import pi, sin
from time import sleep

from sbot import Robot, BRAKE, COAST


def test_motor(r: Robot):
    """Test the motor board."""
    print(f"Name: {r.motor_board.name}")
    print(f"Serial: {r.motor_board.serial_number}")
    print(f"FW: {r.motor_board.firmware_version}")

    print("Increasing to full power, then coasting")
    for i in range(2):
        r.motor_board.motors[i].power = 0.5
    sleep(1)
    for i in range(2):
        r.motor_board.motors[i].power = 1
    sleep(3)
    for i in range(2):
        r.motor_board.motors[i].power = COAST

    sleep(2)

    print("Increasing to full power (reverse), then coasting")
    for i in range(2):
        r.motor_board.motors[i].power = -0.5
    sleep(1)
    for i in range(2):
        r.motor_board.motors[i].power = -1
    sleep(3)
    for i in range(2):
        r.motor_board.motors[i].power = COAST

    sleep(2)

    print("Setting to half power, then braking")
    for i in range(2):
        r.motor_board.motors[i].power = 0.3
    sleep(2)
    for i in range(2):
        r.motor_board.motors[i].power = BRAKE

    sleep(1)

    print("Setting to half power (reverse), then braking")
    for i in range(2):
        r.motor_board.motors[i].power = -0.3
    sleep(2)
    for i in range(2):
        r.motor_board.motors[i].power = BRAKE

    sleep(1)

    print("Setting to half power, then make safe")
    for i in range(2):
        r.motor_board.motors[i].power = 0.5
    sleep(2)
    r.motor_board.make_safe()

    sleep(1)

    for n in range(0, 630, 4):
        p = sin(n / 100)
        print(f"Setting Motor Power to {p}")
        for i in range(2):
            r.motor_board.motors[i].power = p
        sleep(0.1)
