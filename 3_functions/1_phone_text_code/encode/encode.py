def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    # Создание словаря {символ: код}
    punctuation_char = [" ", ".", ",", "?", "!", ":", ";"]
    ru_alphabet = [chr(i) for i in range(1072, 1104)]
    key_list = punctuation_char + ru_alphabet
    value_list = ["0"]

    for code in range(1, 10):
        if code == 1:
            for i in range(1, 7):
                value_list.append(str(code) * i)
        else:
            for i in range(1, 5):
                value_list.append(str(code) * i)

    charset = {char: code for char, code in zip(key_list, value_list)}

    # Кодирование
    result = []
    try:
        for symbol in text:
            result.append(charset[symbol])
        return " ".join(result)
    except KeyError:
        return None
