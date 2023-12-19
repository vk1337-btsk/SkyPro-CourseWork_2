import requests
from random import choice
from basic_word import BasicWord


def load_random_word(address_url):
    """ Функция для получения случайного слова из json файла в облаке \n"""

    # Получаем список слов с внешнего ресурса и выбираем случайное слово
    response = requests.get(address_url)
    random_word = choice(response.json())

    # создаём экземпляр класса BasicWord
    original_word = BasicWord(random_word['word'], random_word['subwords'])

    return original_word