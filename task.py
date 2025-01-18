class Task:
    def __init__(self, name_task, description, deadline, status="Не выполнено"):
        self.name_task = name_task
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        """Изменить статус задачи на 'Выполнено'."""
        if self.status == "Не выполнено":
            self.status = "Выполнено"
            print("Задача выполнена.")
        else:
            print("Эта задача уже выполнена.")

    def show_info(self):
        """Показать информацию о задаче."""
        print(f"Название задачи: {self.name_task}")
        print(f"Описание задачи: {self.description}")
        print(f"Срок выполнения задачи: {self.deadline}")
        print(f"Статус задачи: {self.status}")


# Создаем список для хранения всех задач
tasks = []


def add_new_task():
    """Функция для добавления новой задачи."""
    name_task = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    deadline = input("Введите срок до которого нужно выполнить задачу: ")

    # Добавляем новую задачу в список
    tasks.append(Task(name_task, description, deadline))
    print("Задача успешно добавлена!")


def change_task_status(task_index):
    """Функция для изменения статуса задачи."""
    try:
        task = tasks[task_index]
        task.mark_as_done()
    except IndexError:
        print("Неверный индекс задачи.")


def list_unfinished_tasks():
    """Функция для вывода списка невыполненных задач."""
    for index, task in enumerate(tasks):
        if task.status == "Не выполнено":
            print(f"{index + 1}. Название задачи: {task.name_task}")
            print(f"   Описание задачи: {task.description}")
            print(f"   Срок выполнения задачи: {task.deadline}")
            print(f"   Статус задачи: {task.status}\n")


def list_finished_tasks():
    """Функция для вывода списка выполненных задач."""
    for index, task in enumerate(tasks):
        if task.status == "Выполнено":
            print(f"{index + 1}. Название задачи: {task.name_task}")
            print(f"   Описание задачи: {task.description}")
            print(f"   Срок выполнения задачи: {task.deadline}")
            print(f"   Статус задачи: {task.status}\n")


def main_menu():
    """Основной цикл программы."""
    while True:
        print("\nМеню:")
        print("1. Добавить новую задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать список текущих задач")
        print("4. Показать список выполненных задач")
        print("0. Выход")

        choice = int(input("Ваш выбор: "))

        if choice == 1:
            add_new_task()
        elif choice == 2:
            if len(tasks) > 0:
                task_index = int(input("Введите номер задачи: ")) - 1
                change_task_status(task_index)
            else:
                print("У вас пока нет задач.")
        elif choice == 3:
            list_unfinished_tasks()
        elif choice == 4:
            list_finished_tasks()
        elif choice == 0:
            break
        else:
            print("Неправильный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main_menu()