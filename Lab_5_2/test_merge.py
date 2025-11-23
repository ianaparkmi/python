import pytest
from lab_5_2_5 import merge

def test_simple_merge():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert merge(dict1, dict2) == expected

def test_recursive():
    dict1 = {"a": 1, "b": {"c": 1, "f": 4}}
    dict2 = {"d": 1, "b": {"c": 2, "e": 3}}
    expected = {"a": 1, "b": {"c": 2, "f": 4, "e": 3}, "d": 1}
    assert merge(dict1, dict2) == expected

def test_empty():
    assert merge({}, {}) == {}
    assert merge({'a': 1}, {}) == {'a': 1}