from abc import ABC, abstractmethod

class Parser(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def parse(self, file):
        pass