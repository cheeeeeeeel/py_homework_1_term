from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Функция-генератор разбивает итерируемый объект obj на кортежи длиной n,
    itr - номер итерации, индекс создаваемого кортежа в последовательности."""
    itr = 0
    while len(obj) / (itr + 1) > n:
        yield tuple(obj[n * itr : n * (itr + 1)])
        itr += 1
    else:
        yield tuple(obj[n * itr : ])


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self.obj = tuple(obj)
        self.obj_len = len(obj)
        self.n = n
        self.iter = 0
        self.flag = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.flag:
            if self.obj_len / (self.iter + 1) > self.n:
                result = self.obj[self.n * self.iter: self.n * (self.iter + 1)]
                self.iter += 1
                return result
            else:
                self.flag = False
                return self.obj[self.n * self.iter:]
        raise StopIteration
