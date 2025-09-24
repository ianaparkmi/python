input1 = input('enter a first list: ').split()
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

common_num=[]
not_in_list2=[]
for num in list1:
    if num in list2 and  num not in common_num:
        common_num.append(num)
    if num not in list2:
        not_in_list2.append(num)

not_in_list1=[]
for num in list2:
    if num not in list1:
        not_in_list1.append(num)

all_except_common = []
for num in list1+list2:
    if num not in common_num and num not in all_except_common:
        all_except_common.append(num)

print(" Numbers present in both sets:", common_num)
print(" Numbers only in the first set:", not_in_list2)
print(" Numbers only in the second set:", not_in_list1)
print(" All numbers except common ones:", all_except_common)
