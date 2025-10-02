word1=input("enter a word1").replace(" ",'')
letters1 = list(word1)
word2=input("enter a word2").replace(" ",'')
letters2 = list(word2)
answer=True
if len(letters1) != len(letters2):
   answer=False
for letter in letters1:
    if letters1.count(letter) != letters2.count(letter):
        answer=False
        break 
print(answer)
