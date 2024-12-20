# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])

from datetime import datetime, timedelta
from typing import Callable

def retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exception)] = (Exception,)):
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

            for cnt in range(count):
                try:
                    result = func(*args, **kwargs)
                    return result
                except handled_exceptions:
                    if cnt == count - 1:
                        raise
                    end_sleep = datetime.now() + delay
                    while datetime.now() <= end_sleep:
                        pass

        return wrapper

    return decorator
