from logging import Manager
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
manager.add_task("Включить ноутбук", 2)
manager.add_task("Начать делать проект", 3)
manager.add_task("Закончить делать проект", 3)
manager.add_task("Выключить ноутбук", 1)


if __name__ == "__main__":
    manager.show_tasks()
