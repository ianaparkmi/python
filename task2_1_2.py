numbers_input=input('enter a number and use a spase:').split()
numbers=[]
float_num=[]
for num_str in numbers_input:
    if '.' in num_str:
        numbers.append(float(num_str))
        float_num.append(num_str)
    else:
        numbers.append(int(num_str))
max=numbers[0]
min=numbers[0]
unique_numbers = []
again_num=[]
even=[]
odd=[]
negative_num=[]
sum_5=0
for num in numbers:
    if num not in numbers:
        unique_numbers.append(num)
    else:
          if num not in again_num: 
            again_num.append(num)
    if num % 2==0:
        even.append(num)
    else:
        odd.append(num)
    if num<0:
        negative_num.append(num)
    if num % 5==0:
        sum_5 +=num
    if num>max:
        max=num
    if num<min:
        min=num

print("unique numbers:", unique_numbers)
print(" repeating numbers:", again_num)
print('even numbers:', even)
print('odd numbers:', odd)
print('negative numbers:', negative_num)
print('float numbers:', float_num)
print('Sum of multiples of 5:',sum_5)
print("max number: ", max)
print("min number: ", min)