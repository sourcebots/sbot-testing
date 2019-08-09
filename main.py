"""SBot Non-Interactive Testing Script."""
from time import sleep

from arduino import test_arduino
from metadata import test_metadata
from motor import test_motor
from power import test_power
from servo import test_servo

print("SBot Non-Interactive Testing Script.")

print("Importing Libraries.")

from sbot import *

assert Robot is not None

print("Starting Robot.")

r = Robot(debug=True)

test_functions = [
    test_metadata,
    test_motor,
    test_servo,
    test_arduino,
    test_power,
]

for f in test_functions:
    print(f"Running {f.__name__}")
    f(r)

print("Waiting.")
while True:
    r.power_board.piezo.buzz(0.5, 1000)
    sleep(1)