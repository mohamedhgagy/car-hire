from core import *

"""
    1) create cars
    2) create customers
    3) create booking
    4)create invoice
    5)confirm booking
"""

car1 = Car(name='fait 128', licence_no='asd 123', type=VechileType.FAIT.value,
          category=CarCategory.SMALL.value)

customer1 = Customer('mohamed', 'male', 25, 21223223343)

booking1 = BookingManagment() # create empty instance

invoice1 = Invoice(name='INV/0001',customer=customer1, vechile=car1, book_no=booking1,
                   amount=1500.00)

booking1.create_booking(start_date='1-1-2023', end_date='5-1-2023',
                        vechile=car1, customer=customer1, invoice=invoice1)
booking1.cancel()


print(car1.booking_status)