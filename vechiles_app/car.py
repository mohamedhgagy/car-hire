from .vechile import Vechile
class Car(Vechile):
    def __init__(self, name, licence_no, type, category) -> None:
        super().__init__(name, licence_no, type)
        self.category = category