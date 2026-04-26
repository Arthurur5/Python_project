from rich.prompt import Prompt

from manager import TaskManager


manager = TaskManager()
# manager.add_task("Включить ноутбук", 2)
# manager.add_task("Начать делать проект", 3)
# manager.add_task("Закончить делать проект", 3)
# manager.add_task("Выключить ноутбук", 1)


if __name__ == "__main__":
    while True:
        command = Prompt.ask(
            "Введи команду",
            choices=["show", "add", "delete", "stop", "check", "clear_done"],
            default="show",
        )
        if command == "show":
            manager.show_tasks()
        elif command == "add":
            title: str = Prompt.ask("Введи название")
            priority: str = Prompt.ask("Введи приоритет")
            manager.add_task(title, int(priority))
        elif command == "delete":
            id = int(Prompt.ask("Введи id"))
            manager.delete_task(id)
        elif command == "clear_done":
            manager.clear_done_tasks()
        elif command == "check":
            id = int(Prompt.ask("Введи id"))
            manager.check(id)
        elif command == "stop":
            break
