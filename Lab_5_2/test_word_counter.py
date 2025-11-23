import pytest
from lab_5_2_1 import count_words

def test_basic():
    assert count_words(" hello teacher") == 2

def test_empty():
    assert count_words("")== 0
    assert count_words(" ") ==0

def test_a_lot_of_spaces():
    assert count_words (' i use a lot of spaces') == 6

def test_single_word():
    assert count_words('hi')==1

@pytest.mark.parametrize("text,expected",[
    ('',0),
    ("hi",1),
    ("hi dad",2),
    ('hi     dad',2)
])
def test_parametrize(text, expected):
    assert count_words(text)== expected