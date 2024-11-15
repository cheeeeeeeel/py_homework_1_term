
def encode_text(text: str) -> str | None:
    """Функция, преобразующая текст в код."""
    encode_dict = create_encode_dict()
    result = []
    try:
        for symbol in text:
            result.append(encode_dict[symbol])
        return " ".join(result)
    except KeyError:
        return None

def create_encode_dict() -> dict[str, str]:
    key_list = create_char_list()
    value_list = create_code_list()
    return {char: code for char, code in zip(key_list, value_list)}

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