from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from typing import List

from task import Task


class TaskManager:
    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, priority: int) -> Task:
        task = Task(id=self._next_id, title=title, priority=priority, status=False)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def delete_task(self, id: int) -> None:
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)

    def get_all(self) -> List[Task]:
        return self._tasks.copy()

    def show_tasks(self) -> None:
        table = Table(title="Мои задачи")
        table.add_column("ID", style="cyan")
        table.add_column("Название", style="yellow")
        table.add_column("Приоритет", style="magenta")
        table.add_column("Статус", style="green")

        for task in self._tasks:
            table.add_row(
                str(task.id),
                task.title,
                str(task.priority),
                "1" if task.status else "0",
            )
        Console().print(table)


manager = TaskManager()
# manager.add_task("Включить ноутбук", 2)
# manager.add_task("Начать делать проект", 3)
# manager.add_task("Закончить делать проект", 3)
# manager.add_task("Выключить ноутбук", 1)


if __name__ == "__main__":
    while True:
        command = Prompt.ask(
            "Введи команду", choices=["show", "add", "delete", "stop"], default="show"
        )
        if command == "show":
            manager.show_tasks()
        elif command == "add":
            title = Prompt.ask("Введи название")
            priority = Prompt.ask("Введи приоритет")
            manager.add_task(title, int(priority))
        elif command == "delete":
            id = int(Prompt.ask("Введи id"))
            manager.delete_task(id)
        elif command == "stop":
            break
