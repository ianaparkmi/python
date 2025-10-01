def merge_sorted_list(list_1, list_2):
    result=[]
    i=0
    j=0
    while i<len(list_1) and j<len(list_2):
        if list_1[i]<list_2[j]:
            result.append(list_1[i])
            i+=1
        else:
            result.append(list_2[j])
            j+=1
    while i < len(list_1):
        result.append(list_1[i])
        i += 1
        
    while j < len(list_2):
        result.append(list_2[j])
        j += 1
    return result

def sorted_lst(list):
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j]>list[j+1]:
                list[j], list[j+1]= list[j+1], list[j]
    return list

print("enter a numbers for list 1:")
list_1=list(map( int, input().split()))  
print("enter a numbers for list 2:")
list_2=list(map( int, input().split()))

sorted_list_1=sorted_lst(list_1)
sorted_list_2=sorted_lst(list_2)

print("sorted list 1: ",sorted_list_1)
print("sorted list 2: ",sorted_list_2)
merge_list=merge_sorted_list(sorted_list_1, sorted_list_2)
print('result:', merge_list)