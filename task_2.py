def merge (dict_1, dict_2):
    for key, value in dict_2.items():
        if key in dict_1:
            if isinstance(dict_1[key],dict) and isinstance(value,dict):
                merge(dict_1[key], value)
            elif isinstance(dict_1[key],list) and isinstance(value,list):
                dict_1[key].extend(value)
            elif isinstance(dict_1[key], set) and isinstance(value, set):
                dict_1[key].update(value)
            elif isinstance(dict_1[key], tuple) and isinstance(value, tuple):
                dict_1[key] = dict_1[key] + value
            else:
                dict[key]=value
    return dict_1

dict_1 = {"a": 1, "b": {"c": 1, "f": 4}}
dict_2 = {"d": 1, "b": {"c": 2, "e": 3}}
result = merge(dict_1, dict_2)
print(result)