from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Бесконечно повторяет элементы заданной последовательности."""
    saved = []
    for elem in obj:
        yield elem
        saved.append(elem)

    while saved:
        yield from saved


class Cycle:
    def __init__(self, obj: Iterable[T]):
        self._obj = iter(obj)
        self._iter = None
        self._saved = []
        self._ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._obj:
            try:
                elem = next(self._obj)
                self._saved.append(elem)
                return elem
            except StopIteration:
                if not self._saved:
                    raise
                self._obj = None

        elem = self._saved[self._ind]
        self._ind = (self._ind + 1) % len(self._saved)
        return elem
