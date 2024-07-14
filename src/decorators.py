from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Запись вызова функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


@log()
def my_function(x, y):
    return x + y


#my_function("1", 2)
