def palindrome(input_string):
    string = str(input_string) 
    string=string.replace(' ','').lower()
    return string==string[::-1]
