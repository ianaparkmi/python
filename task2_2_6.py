def unique_elements(lst):
    unique = set()
    for value in lst:
        if type(value) == list:
            nested_unique = unique_elements(value)
            unique.update(nested_unique)
        else:
            unique.add(value)
    return list(unique)


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))