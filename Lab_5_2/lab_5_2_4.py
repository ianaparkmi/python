def anagram (word1, word2):
    word1=word1.replace(" ",'').lower()
    letters1 = list(word1)
    word2=word2.replace(" ",'').lower()
    letters2 = list(word2)
    if len(letters1) != len(letters2):
        return False
    for letter in letters1:
        if letters1.count(letter) != letters2.count(letter):
            return False
    return True