from core import Base
class Customer(Base):
    def __init__(self, name, gender, age, ssn) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.ssn = ssn