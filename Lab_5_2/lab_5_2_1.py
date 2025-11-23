def count_words(sentence):
    if not sentence or sentence.isspace():
        return 0
    return len(sentence.split())