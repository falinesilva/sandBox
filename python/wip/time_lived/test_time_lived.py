import pytest
from time_lived import minutes


def test_minutes_a():
    with pytest.raises(SystemExit):
        minutes("cat")
