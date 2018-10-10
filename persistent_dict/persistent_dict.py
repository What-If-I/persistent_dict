"""
Нужно определить структуру данных реализующую интерфейс словаря (dict), хранение всех
данных в словаре организовать в каком-то временном файле (персистентный словарь).

В идеале:
·         Иметь тесты
·         Возможность установить пакет с помощью setuptools
·         Расширяемый, поддерживаемый код
"""
import os
import pickle
from collections import UserDict
from typing import Optional

__all__ = ['PersistentDict']


class FileStorage:

    def __init__(self, location):
        self.storage_file = location
        if not os.path.exists(self.storage_file):
            open(self.storage_file, 'wb').close()

    def load(self) -> dict:
        with open(self.storage_file, 'rb') as fh:
            data = fh.read()
        return pickle.loads(data) if data else {}

    def save(self, data: dict):
        with open(self.storage_file, 'wb') as fh:
            fh.write(pickle.dumps(data))

    def clear(self):
        os.remove(self.storage_file)


class PersistentDict(UserDict):
    """Dictionary that saves its state into a file"""
    _default_location = os.path.abspath(os.path.dirname(__name__)) + '/storage.file'
    _storage_cls = FileStorage

    def __init__(self, *args, location: Optional[str]=None, **kwargs):
        self._storage = self._storage_cls(location or self._default_location)
        super().__init__(*args, **kwargs)
        if not self.data:
            self.data = self._storage.load()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._storage.save(self.data)

    def clear(self):
        super().clear()
        self._storage.clear()

