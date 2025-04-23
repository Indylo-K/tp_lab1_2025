tasks = []

def strikethrough(text):
    return ''.join(char + '\u0336' for char in text)

def show_tasks():
    if not tasks:
        print("Список порожній.")
    else:
        for i, task in enumerate(tasks, 1):
            text = strikethrough(task["text"]) if task["done"] else task["text"]
            print(f"{i}. {text}")

def add_task():
    text = input("Введіть опис завдання: ")
    tasks.append({"text": text, "done": False})
    print("Завдання додано.")

def mark_done():
    show_tasks()
    try:
        num = int(input("Номер завдання для позначення як виконане: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Завдання позначено як виконане.")
        else:
            print("Неправильний номер.")
    except ValueError:
        print("Введіть число.")

def mark_active():
    show_tasks()
    try:
        num = int(input("Номер завдання для повернення до активних: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = False
            print("Завдання знову активне.")
        else:
            print("Неправильний номер.")
    except ValueError:
        print("Введіть число.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Номер завдання для видалення: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Завдання '{removed['text']}' видалено.")
        else:
            print("Неправильний номер.")
    except ValueError:
        print("Введіть число.")

while True:
    print("\nМеню:")
    print("1. Додати завдання")
    print("2. Переглянути всі завдання")
    print("3. Позначити завдання як виконане")
    print("4. Повернути завдання до активних")
    print("5. Видалити завдання")
    print("6. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        mark_active()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
