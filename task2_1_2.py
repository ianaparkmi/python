numbers_input = input('Enter numbers separated by space: ').split()
numbers = []
float_num = []

for num_str in numbers_input:
    if '.' in num_str:
        num = float(num_str)
        numbers.append(num)
        float_num.append(num)
    else:
        num = int(num_str)
        numbers.append(num)

if not numbers:
    print("No numbers entered!")
    exit()

max_num = numbers[0]
min_num = numbers[0]
unique_numbers = []
again_num = []
even = []
odd = []
negative_num = []
sum_5 = 0

for num in numbers:
    if numbers.count(num) == 1:
        if num not in unique_numbers:
            unique_numbers.append(num)
    else:
        if num not in again_num:
            again_num.append(num)
    
    if isinstance(num, int):
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    if num < 0:
        negative_num.append(num)
    
    if isinstance(num, int) and num % 5 == 0:
        sum_5 += num
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("\n=== ANALYSIS RESULTS ===")
print("1. Unique numbers:", unique_numbers)
print("2. Repeating numbers:", again_num)
print("3. Even numbers:", even)
print("   Odd numbers:", odd)
print("4. Negative numbers:", negative_num)
print("5. Float numbers:", float_num)
print("6. Sum of multiples of 5:", sum_5)
print("7. Max number:", max_num)
print("8. Min number:", min_num)
