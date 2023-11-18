from .vechile import Vechile

class Van(Vechile):
    def __init__(self, name, licence_no, type) -> None:
        super().__init__(name, licence_no, type)