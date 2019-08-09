"""SBot Non-Interactive Testing Script."""

from arduino import test_arduino
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
    test_motor,
    test_servo,
    test_arduino,
    test_power,
]

for f in test_functions:
    print(f"Running {f.__name__}")
    f(r)