numbers=[int(num) for num  in input('enter numbers:').split()]
max=numbers[0] 
max_2=None
for num in numbers:
    if num>max:
        max_2=max
        max=num
    elif max_2 is None:
        if num != max:
            max_2=num
print("The second largest number is:", max_2)