import pytest
from seasons import minutes


def test_minutes_a():
    with pytest.raises(SystemExit):
        minutes("cat")
