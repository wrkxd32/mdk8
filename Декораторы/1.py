import time
from functools import wraps

#1
def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

#2
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

#3
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения '{func.__name__}': {end_time - start_time:.4f} с")
        return result
    return wrapper

#4
def requires_permission(priv):
    def decorator(func):
        @wraps(func)
        def wrapper(polzovat_priv, *args, **kwargs):
            if priv in polzovat_priv:
                return func(*args, **kwargs)
            else:
                raise privError(f"Нет прав у привелегии {priv}")
        return wrapper
    return decorator
