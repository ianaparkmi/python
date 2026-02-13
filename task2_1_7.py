text=input("enter a text")
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

result=''
for char in text:
    if char in char_count:
        result+=char + str(char_count[char])
        del char_count[char]
print('string:', result)
