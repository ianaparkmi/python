import pytest
from lab_5_2_2 import find_unique

def test_complex_nested_structure():
    complex_list = [1, [2, 3], [1, [4, 5]], 6, [7, [8, [9, 1]]]]
    result = find_unique(complex_list)
    expected = [2, 3, 4, 5, 6, 7, 8, 9]
    assert sorted(result) == sorted(expected)

def test_empty():
    assert find_unique([]) == []
    assert find_unique([[]]) == []

def test_single_element():
    assert find_unique([5]) == [5]
    assert find_unique([[5]]) == [5]
    assert find_unique([[[5]]]) == [5]

def test_simple():
    assert find_unique([1, 2, 2, 3]) == [1, 3]

def test_mixed_types():
    assert find_unique([1, 'a', 1, 'b', 'a']) == ['b']
    

