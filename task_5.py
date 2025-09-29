def cache(func):
    cached_results = {}
    def wrapper(*args,**kwargs):
        key=(__name__, args, tuple(kwargs.items()))
        if key in cached_results:
            print(f'use cash: {func.__name__}{args}')
            return cached_results[key]
        else:
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result
    return wrapper

@cache
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2, 3))  