def decode_numbers(numbers: str) -> str | None:
    """Функция, преобразующая код в текст."""
    decode_dict = create_decode_dict()

    chars = []
    try:
        for number in numbers.split():
           chars.append(decode_dict[number])
        return "".join(chars)
    except KeyError:
        return None

def create_decode_dict() -> dict[str, str]:
    key_list = create_code_list()
    value_list = create_char_list()
    return {code: char for code, char in zip(key_list, value_list)}

def create_code_list() -> list[str]:
    list_ = ["0"]
    for digit in range(1, 10):
        if digit == 1:
            for i in range(1, 7):
                list_.append(str(digit) * i)
        else:
            for i in range(1, 5):
                list_.append(str(digit) * i)
    return list_

def create_char_list() -> list[str]:
    punctuation_char = [" ", ".", ",", "?", "!", ":", ";"]
    ru_alphabet = [chr(i) for i in range(1072, 1104)]
    return punctuation_char + ru_alphabet