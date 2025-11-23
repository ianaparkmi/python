def find_unique(lst):
    def  flatten(nested_list):
        result=[]
        for item in nested_list:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_list = flatten(lst)
    count={}
    for i in flat_list:
        count[i]=count.get(i, 0) + 1
    return [i for i in flat_list if count[i]==1]

