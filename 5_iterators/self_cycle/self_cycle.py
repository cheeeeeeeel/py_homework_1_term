from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """
    Функция создает бесконечный генератор благодаря зацикливанию одного объекта. \n
    За последним элементом переданного объекта следует первый.
    """
    while True:
        yield from obj


class Cycle:
    def __init__(self, obj: Iterable[T]):
        self.obj = tuple(obj)
        self.len = len(obj)
        self.ind_obj = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind_obj < self.len:
            res = self.obj[self.ind_obj]
            self.ind_obj += 1
            return res
        elif self.ind_obj == self.len:
            self.ind_obj = 1
            return self.obj[0]
