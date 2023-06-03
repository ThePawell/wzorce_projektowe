from builder import Builder
from drink import Drink


class DrinkBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._product = Drink()

    @property
    def product(self) -> Drink:
        product = self._product
        self.reset()
        return product

    def add_cup(self) -> None:
        self._product.add("Kubek")

    def add_water(self) -> None:
        self._product.add("Wodę")

    def add_tea(self) -> None:
        self._product.add("Herbatę")

    def add_sugar(self) -> None:
        self._product.add("Cukier")

    def add_coffee(self) -> None:
        self._product.add("Kawę")
    def add_milk(self) -> None:
        self._product.add("Mleko")

    def add_chocolate(self) -> None:
        self._product.add("Czekoladę")
