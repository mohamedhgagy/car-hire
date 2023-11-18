from enum import Enum

class BookingStatus(Enum):
    PENDING = 0
    BOOKED = 1
    CANCELED = 2