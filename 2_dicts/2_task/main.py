import re

def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    most_common = {}
    words = re.findall(r"\w{3,}", text.lower())

    for word in words:
        if word in most_common:
            most_common[word] += 1
        else:
            most_common[word] = 1

    most_common = sorted(most_common.items())
    most_common = dict(
        sorted(most_common, key=lambda pair: -pair[1])[:10]
    )
    return most_common
