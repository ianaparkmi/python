def merge(dict1, dict2):
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key].extend(value)
            elif isinstance(result[key], set) and isinstance(value, set):
                result[key].update(value)
            elif isinstance(result[key], tuple) and isinstance(value, tuple):
                result[key] = result[key] + value
            else:
                result[key] = value
        else:
            result[key] = value
    
    return result