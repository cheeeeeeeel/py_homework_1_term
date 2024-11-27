import re

def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """

    words = re.findall(r"\w{3,}", text.lower())

    word_count = {}
    for word in set(words):
        word_count[word] = words.count(word)

    most_common = sorted(word_count.items(), key=lambda pair: (-pair[1], pair[0]))[:10]
    return dict(most_common)
