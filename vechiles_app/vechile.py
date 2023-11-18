class Vechile:
    def __init__(self, name, licence_no, type) -> None:
        self.name = name
        self.licence_no = licence_no
        self.type = type
        self.booking_status = None
    
    def __str__(self) -> str:
        return f'[{self.licence_no}] {self.name}'
    
        
