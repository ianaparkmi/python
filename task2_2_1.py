def flatten(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten(lst[i])  
            lst[i:i+1] = lst[i]  
        else:
            i += 1

list_a = [1, 14, 3, [9], 5, [6, [6, [], 8, 9]]]
print("До:", list_a)
flatten(list_a)
print("После:", list_a)