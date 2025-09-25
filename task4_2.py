nput1 = input('enter a first list: ').split()
list1=[]
for num in input1:
    if "." in num:
        list1.append(float(num))
    else:
        list1.append(int(num))

input2 = input('enter a first list: ').split()
list2=[]
for num in input2:
    if "." in num:
        list2.append(float(num))
    else:
        list2.append(int(num))

set1=set(list1)
set2=set(list2)
common_numbers = set1 & set2
only_in_first = set1 - set2
only_in_second = set2 - set1
all_except_common = set1 ^ set2

print(" Numbers present in both sets:", common_numbers)
print(" Numbers only in the first set:", only_in_first)
print(" Numbers only in the second set:", only_in_second)
print(" All numbers except common ones:", all_except_common)