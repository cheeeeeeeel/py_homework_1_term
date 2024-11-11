import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)

from decimal import Decimal
def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    _ = get_employees_info()
    parsed_employees_info = []

    # Ваш код ниже
    right_keys = ["id", "name", "last_name", "age", "salary", "position"]
    for sentence in _:

        by_word = sentence.split()
        employee_info = {}

        for idx in range(len(by_word)):
            if by_word[idx] in right_keys:
                employee_info[by_word[idx]] = by_word[idx + 1]

        employee_info["id"], employee_info["age"] = int(employee_info["id"]), int(employee_info["age"])
        employee_info["salary"] = Decimal(employee_info["salary"])

        parsed_employees_info.append(employee_info)
    return parsed_employees_info
