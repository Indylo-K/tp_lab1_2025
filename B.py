import random

words = [
    "алгоритм", "компілятор", "інтерфейс", "память", "массив", "цикл", "функція", "змінна",
    "дебаг", "гілка", "синтаксис", "команда", "мова", "код", "відладка", "структура",
    "платформа", "середовище", "сценарій", "тип", "рядок", "обʼєкт", "бібліотека", "індекс",
    "ключ", "модуль", "оператор", "виклик", "помилка", "логіка"
]

TRIES = 7

def get_random_word():
    return random.choice(words)

def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    word = get_random_word()
    guessed_letters = []
    tries_left = TRIES

    print("Гра 'Вгадай слово'")

    while tries_left > 0:
        print("\nСлово:", display_current_state(word, guessed_letters))
        print("Залишилось спроб:", tries_left)

        guess = input("Введіть літеру або ціле слово: ").lower().strip()

        if len(guess) == 0:
            print("Введення не може бути порожнім.")
            continue

        if len(guess) > 1:
            if guess == word:
                print("Ви вгадали слово:", word)
                break
            else:
                print("Неправильно. Це не те слово.")
                tries_left -= 1
                continue

        if guess in guessed_letters:
            print("Ви вже вводили цю літеру.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            if all(letter in guessed_letters for letter in word):
                print("Ви вгадали слово:", word)
                break
        else:
            print("Неправильно.")
            tries_left -= 1

    else:
        print("Гру завершено. Ви програли.")
        print("Загадане слово було:", word)

while True:
    play_game()
    again = input("Бажаєте зіграти ще раз? (так/ні): ").strip().lower()
    if again != "так":
        break
