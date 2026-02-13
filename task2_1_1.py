text=input('enter a text')
words=text.split()
word_count={}
for word in words:
    word_lower=word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1
unique_words_count = len(word_count)
print("\n1. Word frequency dictionary:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

print(f"\n2. Number of unique words: {unique_words_count}")