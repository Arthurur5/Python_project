from rich.prompt import Prompt

from manager import TaskManager


manager = TaskManager()

if __name__ == "__main__":
    while True:
        command: str = Prompt.ask(
            "Введи команду",
            choices=["show", "add", "delete", "stop", "check", "change", "clear_done"],
            default="show",
        )
        if command == "show":
            manager.show_tasks()
        elif command == "add":
            title: str = Prompt.ask("Введи название")
            priority: int = int(Prompt.ask("Введи приоритет"))
            manager.add_task(title, priority)
        elif command == "delete":
            id = int(Prompt.ask("Введи id"))
            manager.delete_task(id)
        elif command == "clear_done":
            manager.clear_done_tasks()
        elif command == "check":
            id = int(Prompt.ask("Введи id"))
            manager.check(id)
        elif command == "change":
            id = int(Prompt.ask("Введи id"))
            new_title: str = Prompt.ask("Введи новое название (enter чтобы оставить)")
            new_priority: str = Prompt.ask("Введи приоритет (enter чтобы оставить)")
            manager.change_task(id, new_title, new_priority)
        elif command == "stop":
            break
