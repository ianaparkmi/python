import pytest 
from lab_5_2_3 import palindrome

@pytest.mark.parametrize("input,expected",[
    ("радар", True),
    ("a", True),
    ("", True),
    ('dog', False),
    (121, True),
    (10, False),
])

def test_palindrome(input, expected):
    assert palindrome(input) == expected