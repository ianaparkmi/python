def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            if len(types) != len(args):
                raise TypeError(f"Ожидается {len(types)} аргументов, получено {len(args)}")
            for i in range(len(args)):
                arg = args[i]
                expected_type = types[i]
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {i} должен быть {expected_type.__name__}, получен {type(arg).__name__}")
            print("Все аргументы корректны!")
            
            return func(*args)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))     
print(add(5, "hello"))   
print(add(9)) 