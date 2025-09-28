import time

def timing(func):
    def wrapper():
        start = time.time()
        result = func()  
        end = time.time()
        print(f"Время выполнения: {(end - start) * 1000:.2f} мс")
        return result
    return wrapper

@timing
def count_to_million():
    total = 0
    for i in range(1000000):
        total += i
    return total

count_to_million()