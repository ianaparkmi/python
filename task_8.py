string=input('enter a string')
string=string.replace(' ','').lower()
if string==string[::-1]:
    print("Yes, it's a palindrome")
else:
    print ("It's not a palindrome")