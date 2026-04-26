from rich.console import Console
from rich.table import Table
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

    def check(self, id: int) -> None:
        for task in self._tasks:
            if task.id == id:
                task.status = not task.status

    def change_task(self, id: int, title: str, priority: str) -> None:
        for task in self._tasks:
            if task.id == id:
                if title != "":
                    task.title = title
                if priority != "":
                    task.priority = int(priority)

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
