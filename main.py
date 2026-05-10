from rich.prompt import Prompt
from rich.console import Console

from errors import InvalidPriorityError, TaskNotFoundError
from manager import TaskManager

manager = TaskManager()
console = Console()

if __name__ == "__main__":
    while True:
        command: str = Prompt.ask(
            "Введи команду",
            choices=["show", "add", "delete", "stop", "check", "change", "clear_done"],
            default="show",
        )
        if command == "show":
            sort_key: str = Prompt.ask(
                "Сортировка по параметру",
                choices=["id", "title", "priority"],
                default="id",
            )
            manager.show_tasks(sort_key=sort_key)

        elif command == "add":
            try:
                title: str = Prompt.ask("Введи название")
                priority: int = int(Prompt.ask("Введи приоритет"))
                manager.add_task(title, priority)
            except InvalidPriorityError:
                console.print("[red]Приоритет дожен быть от 1 до 5[/red]")

        elif command == "delete":
            try:
                id = int(Prompt.ask("Введи id"))
                manager.delete_task(id)
            except TaskNotFoundError:
                console.print("[red]Нет задачи с таким ID[/red]")

        elif command == "clear_done":
            manager.clear_done_tasks()

        elif command == "check":
            try:
                id = int(Prompt.ask("Введи id"))
                manager.check(id)
            except TaskNotFoundError:
                console.print("[red]Нет задачи с таким ID[/red]")

        elif command == "change":
            try:
                id = int(Prompt.ask("Введи id"))
                new_title: str = Prompt.ask(
                    "Введи новое название (enter чтобы оставить)"
                )
                new_priority: str = Prompt.ask("Введи приоритет (enter чтобы оставить)")
                manager.change_task(id, new_title, new_priority)
            except TaskNotFoundError:
                console.print("[red]Нет задачи с таким ID[/red]")

        elif command == "stop":
            break
