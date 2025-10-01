user_list=input("enter elements of list and use a space").split()
usee_list=[]
unique_list = []
seen = []
for elem in user_list:
    if elem  not in seen:
        unique_list.append(elem)
        seen.append(elem)
print("list without doublons:", unique_list)