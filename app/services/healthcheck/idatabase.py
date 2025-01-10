from abc import ABCMeta, abstractmethod


class IDatabaseHealthCheck(metaclass=ABCMeta):
    @abstractmethod
    def is_up(self):
        raise NotImplementedError
