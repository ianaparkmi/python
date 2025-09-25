text=input('enter a text')
words=text.split()
word_count={}
for word in words:
    word_lower=word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1