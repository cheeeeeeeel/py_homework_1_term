
def plus(num1: int = None, num2: int = None) -> int:
    """Оператор сложения."""
    if not_none(num1, num2):
        return num1 + num2
    return num1, plus

def minus(num1: int = None, num2: int = None) -> int:
    """Оператор вычитания."""
    if not_none(num1, num2):
        return num1 - num2
    return num1, minus

def times(num1: int = None, num2: int = None) -> int:
    """Оператор умножения."""
    if not_none(num1, num2):
        return num1 * num2
    return num1, times

def divided_by(num1: int = None, num2: int = None) -> int:
    """Оператор целочисленного деления."""
    if num2 == 0:
        return None
    elif not_none(num1, num2):
        return num1 // num2
    return num1, divided_by

def not_none(*args: int | None) -> bool:
    return all(arg is not None for arg in args)


def number(a: int) -> callable:
    """Для заданного числа 'a' реализуется внутренняя функция inner,
    в которой осуществляется арифметическая операция
    при условии, что оператор и правый операнд 'b' заданы."""

    def inner(args: tuple[int, callable] = None) -> int:
        if args:
            b, operator = args
            return operator(a, b)
        return a

    return inner

zero = number(0)
one = number(1)
two = number(2)
three = number(3)
four = number(4)
five = number(5)
six = number(6)
seven = number(7)
eight = number(8)
nine = number(9)
