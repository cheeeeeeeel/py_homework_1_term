from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Бесконечно повторяет элементы заданной последовательности."""
    while True:
        yield from obj

class Cycle:
    def __init__(self, obj: Iterable[T]):
        self._obj = obj
        self._iter = iter(obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            self._iter = self._obj.__iter__()
            return next(self._iter)
