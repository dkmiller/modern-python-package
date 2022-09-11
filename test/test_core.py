from modern_python_package.core import inner_method
import pytest


@pytest.mark.parametrize(
    "string,integer,expected",
    [
        ("a", 1, "a"),
        ("b", 2, "bb"),
        ("ab", 3, "ababab"),
        ("a", 0, ""),
        ("", 3, ""),
        ("c", -2, ""),
    ],
)
def test_inner_method(string, integer, expected):
    value = inner_method(string, integer)

    # Put expected value first:
    # https://stackoverflow.com/a/57059952
    assert expected == value
