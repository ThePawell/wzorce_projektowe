from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_cup(self) -> None:
        pass

    @abstractmethod
    def add_water(self) -> None:
        pass

    @abstractmethod
    def add_tea(self) -> None:
        pass

    @abstractmethod
    def add_sugar(self) -> None:
        pass

    @abstractmethod
    def add_coffee(self) -> None:
        pass

    @abstractmethod
    def add_milk(self) -> None:
        pass

    @abstractmethod
    def add_chocolate(self) -> None:
        pass
