from abc import ABC, abstractmethod


class AbstractAppShape(ABC):

    @abstractmethod
    def run(self):
        pass

    @classmethod
    @abstractmethod
    def getStatusApp(cls):
        pass
