class Task():
    def __init__(self, name_task, about, time_out, status = "Не выполнено"):
        self.name_task = name_task
        self.about = about
        self.time_out = time_out
        self.status = status

    def new_task(self):
        self.name_task = input("Введите название задачи: ")
        self.about = input("Введите описание задачи: ")
        self.time_out = input("Введите срок до которого нужно выполнить задачу: ")
        print("Задача добавлена")

    def new_status(self):
        if self.status == "Не выполнено":
            self.status = "Выполнено"
            print("Задача выполнена")
        elif self.status == "Выполнено":
            self.status = "Не выполнено"
            print("Задача снова считается не выполненной")
        else:
            print("Такой дачи не существует")

    def info(self):
        print(f"Название задачи: {self.name_task}")
        print(f"Описание задачи: {self.about}")
        print(f"Срок выполнения задачи: {self.time_out}")
        print(f"Статус задачи: {self.status}")

