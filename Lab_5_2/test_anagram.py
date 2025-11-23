import pytest
from lab_5_2_4 import anagram

@pytest.mark.parametrize('word1,word2,result',[
    ("anagram", "nagaram", True),      
    ("Dormitory", "Dirty room", True), 
    ("hello", "world", False),         
    ("test", "tests", False),          
    ("", "", True),   
])
def test_anagram(word1,word2,result):
    assert anagram(word1,word2)==result