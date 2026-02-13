user_list=input("enter elements of list and use a space").split()
unique_list = []
for elem in user_list:
    if elem  not in unique_list:
        unique_list.append(elem)
print("list without doublons:", unique_list)