import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_now=datetime.datetime.now()
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f'{time_now}-{func.__name__}- args: {args} - kwargs: {kwargs}')
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log_calls("log.txt")
def multiply(x, y):
    return x * y

multiply(2,4)
        