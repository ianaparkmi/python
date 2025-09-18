number=int(input("Enter a number: "))
if number % 7==0:
    print("magic number!")
else:
    sum = 0
    while number > 0:
        digit = number % 10
        sum+=digit
        number=number//10
    print("sum: ", sum)