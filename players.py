class Player:
    """Класс для работы с данными пользователя, такими как имя пользователя и введённые им слова \n"""

    def __init__(self, user_name: str):
        """Инициализирую переменные: user_name - имя пользователя; words - использованные слова пользователя. \n"""
        self.user_name = user_name
        self.user_words = []

    def __str__(self):
        return self.user_name.capitalize()

    def __repr__(self):
        """ Представление объекта в виде строки (для отладки) \n"""
        return f"""Пользователь с именем: {self.user_name.capitalize()}\n
        \rВвёл следующие слова: {self.user_words}"""

    def get_number_words_in_user_list(self):
        """ Функция для получения количества использованных слов (возвращает int)"""
        return len(self.user_words)

    def add_entered_word_user_list(self, user_word: str):
        """ Функция для добавления введённого слова в использованные слова (ничего не возвращает). \n"""
        self.user_words.append(user_word)
        return

    def checking_presence_entered_word_in_user_list(self, user_word: str):
        """  Функция для проверки использования введённого слова до этого (возвращает bool). \n"""
        return user_word in self.user_words
