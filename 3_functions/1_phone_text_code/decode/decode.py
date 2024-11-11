def decode_numbers(numbers: str) -> str | None:
    """Пишите ваш код здесь."""
    # Создание словаря {код: символ}
    punctuation_char = [" ", ".", ",", "?", "!", ":", ";"]
    ru_alphabet = [chr(i) for i in range(1072, 1104)]
    value_list = punctuation_char + ru_alphabet
    key_list = ["0"]

    for char in range(1, 10):
        if char == 1:
            for i in range(1, 7):
                key_list.append(str(char) * i)
        else:
            for i in range(1, 5):
                key_list.append(str(char) * i)

    charset = {code: char for code, char in zip(key_list, value_list)}

    # Декодирование
    numbers = numbers.split()
    result = ""
    try:
        for letter in numbers:
            result += charset[letter]
        return result
    except KeyError:
        return None
