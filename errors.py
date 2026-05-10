"""Модуль с ошибками"""


class BaseManagerError(Exception):
    """Базовая ошибка"""

    pass


class TaskNotFoundError(BaseManagerError):
    """Задача с таким ID не найдена"""

    pass


class InvalidPriorityError(BaseManagerError):
    """Приоритет должен быть от 1 до 5"""

    pass
