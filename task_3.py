password=input("enter a password:")
if len(password)<16:
    print('your password is too short')
elif password.isalpha() | password.isdigit():
    print('your password is too weak')
else: print('you have a strong password')
