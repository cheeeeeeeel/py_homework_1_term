from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Преобразует данные из итерируемого объекта в кортежи длиной n."""
    if n < 1:
        raise ValueError(f"Invalid value for 'n': {n}. Must be 1 at least.")
    batch = []
    for elem in iter(obj):
        batch.append(elem)
        if len(batch) == n:
            yield tuple(batch)
            batch.clear()
    if batch:
        yield tuple(batch)


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self._iter = iter(obj)
        self._n = self._valid_n(n)

    def __iter__(self):
        return self

    def __next__(self):
        batch = []
        try:
            for _ in range(self._n):
                elem = next(self._iter)
                batch.append(elem)
            return tuple(batch)
        except StopIteration:
            if batch:
                return tuple(batch)
            raise

    def _valid_n(self, n):
        if n < 1:
            raise ValueError(f"Invalid value for 'n': {n}. Must be 1 at least.")
        return n
