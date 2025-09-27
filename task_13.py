import random
number=random.randint(1,100)
print("try to guess a number between 1 and 100")
while True:
    attempt=int(input("enter a number"))
    if attempt>number:
        print("the number is less than you entered")
    elif attempt<number:
        print("the number is higher than you entered")
    else:
        print("you win!")
        break