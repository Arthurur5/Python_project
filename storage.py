"""Сохранение и загрузка задач в JSON."""

import json
from typing import List
from task import Task


class JSONStorage:
    """Работа с JSON-файлом"""

    def __init__(self, filename: str = "tasks.json") -> None:
        self.filename = filename

    def save(self, tasks: List[Task]) -> None:
        """Сохранить задачи в файл"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([task.model_dump() for task in tasks], f, indent=4)

    def load(self) -> List[Task]:
        """Загрузить задачи из файла"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except FileNotFoundError:
            return []
