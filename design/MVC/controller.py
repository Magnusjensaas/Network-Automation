from abc import ABC, abstractmethod
import model

class UserController(ABC):
    def __init__(self, view):
        self.view = view

    @abstractmethod
    def create(self):
        raise  NotImplementedError

    @abstractmethod
    def get(self, id):
        raise NotImplementedError
