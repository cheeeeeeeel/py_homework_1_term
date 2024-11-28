from typing import Callable


def number(operand: int) -> Callable[..., int]:

    def inner(operation: Callable[[int], int]=None):
        if operation:
            return operation(operand)
        return operand

    return inner

# объявление функций-чисел
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


def plus(right_operand: int) -> Callable[[int], int]:

    def addition(left_operand: int) -> int:
        return left_operand + right_operand

    return addition


def minus(right_operand: int) -> Callable[[int], int]:

    def subtraction(left_operand: int) -> int:
        return left_operand - right_operand

    return subtraction


def times(right_operand: int) -> Callable[[int], int]:

    def multiplication(left_operand: int) -> int:
        return left_operand * right_operand

    return multiplication


def divided_by(right_operand: int) -> Callable[[int], int]:

    def division(left_operand: int) -> int:
        if right_operand == 0:
            return None
        return left_operand // right_operand

    return division
