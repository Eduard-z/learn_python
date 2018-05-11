"""
reloadall.py: транзитивная перезагрузка вложенных модулей
"""

import types
from importlib import reload                            # требуется в версии 3.0

def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:                           # Пропустить повторные посещения
        status(module)                                  # Перезагрузить модуль
        reload(module)                                  # И посетить дочерние модули
        visited[module] = None
        for attrobj in module.__dict__.values():        # Для всех атрибутов
            if type(attrobj) == types.ModuleType:       # Рекурсия, если модуль
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall                                    # Тест: перезагрузить самого себя
    reload_all(reloadall)                               # Должна перезагрузить этот модуль и модуль types

"""Чтобы воспользоваться этой утилитой, импортируйте функцию reload_all
и передайте ей имя уже загруженного модуля (как если бы это была встроен-
ная функция reload)."""

from reloadall import reload_all
import os, tkinter
reload_all(os)
reload_all(tkinter)
