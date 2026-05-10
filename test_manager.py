"""Простые Задачаы для Task Manager."""

import pytest
from errors import TaskNotFoundError
from task import Task
from manager import TaskManager


class TestTask:
    def test_create_task(self):
        task = Task(id=1, title="Задача", priority=2, status=False)
        assert task.id == 1
        assert task.title == "Задача"
        assert task.priority == 2
        assert task.status is False

    def test_change_status(self):
        task = Task(id=1, title="Задача", priority=2, status=False)
        task.status = True
        assert task.status is True


class TestTaskManager:
    def setup_method(self):
        self.manager = TaskManager()
        self.manager._tasks.clear()
        self.manager._next_id = 1

    def test_add_task(self):
        task = self.manager.add_task("Добавить задачу", 2)
        assert task.id == 1
        assert task.title == "Добавить задачу"
        assert task.priority == 2
        assert len(self.manager.get_all()) == 1

    def test_delete_task(self):
        self.manager.add_task("Задача", 2)
        self.manager.delete_task(1)
        assert len(self.manager.get_all()) == 0
        with pytest.raises(TaskNotFoundError):
            self.manager.delete_task(1)

    def test_toggle_status(self):
        self.manager.add_task("Задача", 2)
        self.manager.check(1)
        assert self.manager.get_all()[0].status is True
        self.manager.check(1)
        assert self.manager.get_all()[0].status is False
        with pytest.raises(TaskNotFoundError):
            self.manager.check(3)

    def test_change(self):
        self.manager.add_task("Добавить задачу", 2)
        self.manager.change_task(1, title="Убрать задачу", priority=4)
        assert self.manager.get_all()[0].priority == 4
        assert self.manager.get_all()[0].title == "Убрать задачу"

    def test_clear_tasks(self):
        self.manager.add_task("Задача 1", 1)
        self.manager.add_task("Задача 2", 2)
        self.manager.add_task("Задача 3", 3)
        self.manager.check(3)
        self.manager.check(1)
        assert len(self.manager.get_all()) == 3
        self.manager.clear_done_tasks()
        assert len(self.manager.get_all()) == 1
