tasks = []

while True:
    print("\n1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выход")
    choice = input("Выберите действие (1-3): ")

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)
        print("Задача добавлена!")
    elif choice == "2":
        if tasks:
            print("Список задач:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Список задач пуст!")
    elif choice == "3":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор, попробуйте снова!")