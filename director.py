from builder import Builder


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def prepare_cup(self) -> None:
        self.builder.add_cup()

    def prepare_tea(self) -> None:
        self.builder.add_cup()
        self.builder.add_water()
        self.builder.add_tea()
        self.builder.add_sugar()

    def prepare_coffee(self) -> None:
        self.builder.add_cup()
        self.builder.add_water()
        self.builder.add_coffee()

    def prepare_hot_chocolate(self) -> None:
        self.builder.add_cup()
        self.builder.add_milk()
        self.builder.add_chocolate()
        self.builder.add_sugar()

    def prepare_latte(self) -> None:
        self.builder.add_cup()
        self.builder.add_milk()
        self.builder.add_coffee()

