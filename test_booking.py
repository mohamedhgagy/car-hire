import unittest
from core import *

class TestBooking(unittest.TestCase):
    def setUp(self):
        """
        1) create cars
        2) create customers
        3) create booking
        4)create invoice
        5)confirm booking
        """

        self.car1 = Car(name='fait 128', licence_no='asd 123', type=VechileType.FAIT.value,
                category=CarCategory.SMALL.value)

        self.customer1 = Customer('mohamed', 'male', 25, 21223223343)

        self.booking_manager1 = BookingManagment() # create empty instance

        self.invoice1 = Invoice(name='INV/0001',customer=self.customer1, vechile=self.car1, book_no=self.booking_manager1,
                        amount=1500.00)

        self.booking1 = self.booking_manager1.create_booking(start_date='1-1-2023', 
                                                   end_date='5-1-2023', vechile=self.car1, 
                                                   customer=self.customer1, invoice=self.invoice1)


    def test_confrim(self):
        result = self.booking1.confirm()
        self.assertEqual(result, True)

    def test_cancel(self):
        result = self.booking1.cancel()
        self.assertEqual(result, True)

    def test_reset_to_pending(self):
        result = self.booking1.reset_to_pending()
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()