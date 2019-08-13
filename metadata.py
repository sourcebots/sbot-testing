"""SBot Metadata Test Script."""
from sbot import Robot


def test_metadata(r: Robot):
    """Test the metadata."""
    print(f"Competition: {r.is_competition}")
    print(f"Zone: {r.zone}")