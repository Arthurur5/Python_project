"""Модуль с классом TaskManager"""

from rich.console import Console
from rich.table import Table
from typing import List

from task import Task
from storage import JSONStorage
from errors import (
    InvalidPriorityError,
    TaskNotFoundError,
)


class TaskManager:
    """Менеджер для управления задачами"""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1
        self._storage = JSONStorage()
        self._load_from_storage()

    def _load_from_storage(self) -> None:
        tasks: List[Task] = self._storage.load()
        if tasks:
            self._tasks = tasks
            self._next_id = max(t.id for t in tasks) + 1

    def _save_to_storage(self) -> None:
        self._storage.save(self._tasks)

    def add_task(self, title: str, priority: int) -> Task:
        """Добавить задание (название и приоритет от 1 до 5)"""
        if priority > 5 or priority < 1:
            raise InvalidPriorityError
        task = Task(id=self._next_id, title=title, priority=priority, status=False)
        self._tasks.append(task)
        self._next_id += 1
        self._save_to_storage()
        return task

    def delete_task(self, id: int) -> None:
        """Удалить задание по id"""
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                break
        else:
            raise TaskNotFoundError
        self._save_to_storage()

    def clear_done_tasks(self) -> None:
        """Удалить все выполненные задания"""
        for task in self._tasks:
            if task.status == True:
                self._tasks.remove(task)
        self._save_to_storage()

    def check(self, id: int) -> None:
        """Поменять статус задачи"""
        for task in self._tasks:
            if task.id == id:
                task.status = not task.status
                break
        else:
            raise TaskNotFoundError
        self._save_to_storage()

    def change_task(self, id: int, title: str, priority: str) -> None:
        """Изменить задачу по id (название и приоритет, если пустые, то останутся прежними)"""
        for task in self._tasks:
            if task.id == id:
                if title != "":
                    task.title = title
                if priority != "":
                    task.priority = int(priority)
                break
        else:
            raise TaskNotFoundError
        self._save_to_storage()

    def show_tasks(self) -> None:
        """Вывести на экран задания"""
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
