"""Основной файл, в котором выполняется курсовая работа. """

# Импортируем нужные классы и функции.
from players import Player
from utils import load_random_word


# Основной блок программы
if __name__ == '__main__':
    # Переменная - строка ссылка на внешний ресурс
    url_address = "https://www.jsonkeeper.com/b/9WUV"

    # Получаем слово из внешнего ресурса
    original_word = load_random_word(url_address)

    # Получаем имя пользователя и здороваемся с ним
    user = Player(input("Введите имя игрока: "))
    print(f"Привет, {user}!\n")

    # Вы водим слово и правила игры
    print(f"Составьте {original_word.counting_number_subwords()} слов из слова {str(original_word).upper()}")
    print("Слова должны быть не короче 3 букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')

    """
    # Для просмотра и отладки (для проверяющего):
    print(original_word.__repr__())
    """

    # Начинаем игру
    print("Поехали!")
    # Начинаем цикл и прекращаем его только если список подслов равен списку угаданных пользователем
    while True:

        # Проверка на окончание игры (если все слова отгаданы)
        if user.get_number_words_in_user_list() == original_word.counting_number_subwords():
            print(f'Вы молодцы! Вы победили и отгадали все {user.get_number_words_in_user_list()} слов.')
            break

        # Ввод слова
        input_user_word = input("Введите ваше слово: ").lower().strip()

        # Если слово короче 3-х букв
        if len(input_user_word) < 3:
            print('Это слишком короткое слово...')
            continue

        if input_user_word in ["stop", "стоп"]:
            print(f'Игра завершена, вы угадали {user.get_number_words_in_user_list()} слов!')
            break

        # Проверяем есть ли это слово в нашем подсписке
        if original_word.checking_entered_word_in_list(input_user_word):

            # Если есть. Проверяем было ли слово в списке пользователя
            if user.checking_presence_entered_word_in_user_list(input_user_word):
                # Если уже было
                print(f'Слово "{input_user_word}" вы уже отгадали ранее')
                continue

            else:
                # Если ещё не было - добавляем
                print(f'Верно! Вы угадали слово "{input_user_word}"!')
                user.add_entered_word_user_list(input_user_word)
                continue

        else:
            # Если такого слова нет в нашем подсписке
            print(f'Неверно. Слово "{input_user_word}" нельзя составить из загаданного или такого слова не существует.')
            continue
