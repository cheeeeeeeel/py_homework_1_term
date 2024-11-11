"""
Вам дан список предложений.
Предложение содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    """Пишите ваш код здесь."""
    max_num = 0
    for sentence in sentences:
        cur_num = len(sentence.split())
        if cur_num > max_num:
            max_num = cur_num
    return max_num

