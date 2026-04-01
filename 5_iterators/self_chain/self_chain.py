from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Объединяет несколько итерируемых объектов в один последовательный итератор."""
    for obj in iterables:
        yield from obj


class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self._iterables = iter(iterables)
        self._iter = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._iter is None:
                self._iter = iter(next(self._iterables))
            try:
                return next(self._iter)
            except StopIteration:
                self._iter = None
