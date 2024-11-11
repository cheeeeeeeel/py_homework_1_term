from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Генерирует единую цельную последовательность
    из элементов переданных итерируемых объектов."""
    for obj in iterables:
        yield from obj


class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self.objects = iterables
        self.num_objs = len(iterables)
        self.obj_ind = 0
        self.ind_elem = 0
        self.obj = tuple(iterables[self.obj_ind])

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind_elem < len(self.obj):
            res = self.obj[self.ind_elem]
            self.ind_elem += 1
            return res
        else:
            self.obj_ind += 1
            if self.num_objs == self.obj_ind:
                raise StopIteration
            self.ind_elem = 1
            self.obj = tuple(self.objects[self.obj_ind])
            return self.obj[0]
