class BasicWord:
    """Класс для работы с исходным словом, а также всеми возможными подсловами, которые состоят из исходного \n"""

    def __init__(self, original_word: str, words: list):
        """"Инициализирую переменные: original_word - исходное слово; words - набор допустимых подслов. \n"""
        self.original_word = original_word
        self.words = words

    def __str__(self):
        """ Представление объекта в виде строки (для пользователя) \n"""
        return f"{self.original_word}"

    def __repr__(self):
        """ Представление объекта в виде строки (для отладки) \n"""
        return f"""{self.original_word} - исходное слово;
        \r {self.words} - набор допустимых подслов."""

    def counting_number_subwords(self):
        """ Функция для подсчета количества подслов в списке words (возвращает int). \n"""
        return len(self.words)

    def checking_entered_word_in_list(self, user_word):
        """ Функция для проверки введенного слова в списке допустимых подслов (возвращает bool). \n"""
        return user_word in self.words
