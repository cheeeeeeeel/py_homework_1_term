# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])
import time
from datetime import timedelta
from typing import Callable

def retry(count: int, delay: timedelta, handled_exceptions: tuple[type[Exception],] = (Exception,)):
    """
    Декоратор позволяет повторно вызывать функцию:
        1. Заданное количество раз.
        2. С некоторой задержкой после неудачного вызова.
        3. Только в случае возникновения одного из указанных исключений. По дефолту обрабатываются все исключения.
    """
    if count < 1:
        raise ValueError(f"Число попыток не должно быть меньше 1, сейчас {count}")

    def decorator(func: Callable):

        def wrapper(*args, **kwargs):

            for attempt in range(count):
                try:
                    result = func(*args, **kwargs)
                    return result
                except handled_exceptions as e:
                    if attempt == count - 1:
                        raise e
                time.sleep(delay.total_seconds())

        return wrapper

    return decorator
