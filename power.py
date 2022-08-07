"""SBot Power Board Test Script."""
from time import sleep

from sbot import Robot, Note


def test_power(r: Robot):
    print(f"Name: {r.power_board.name}")
    print(f"Serial: {r.power_board.serial_number}")
    print(f"FW: {r.power_board.firmware_version}")

    for i in range(5):
        sleep(1)
        print("Turning on outputs")
        r.power_board.outputs.power_on()
        sleep(1)
        print("Turning off outputs")
        r.power_board.outputs.power_off()

    for note in Note:
        print(f"Playing {note} on buzzer")
        r.power_board.piezo.buzz(1, note)
        sleep(0.2)
    for freq in range(250, 6000, 250):
        print(f"Playing {freq}Hz on buzzer")
        r.power_board.piezo.buzz(0.2, freq)
        sleep(0.2)
