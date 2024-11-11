import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()

    # Ваш код ниже, возвращайте уже отредактированный текст!
    sentences = wrong_article.split('.\n')
    for i, sentence in enumerate(sentences):
        sentence = sentence[::-1]
        sentence = sentence.replace('!', '', len(sentence) // 2)
        sentence = sentence.replace('WOOF-WOOF', 'CAT')
        sentence = sentence.capitalize()
        sentences[i] = sentence
    wrong_article = '.\n'.join(sentences)
    return wrong_article
