from . import BookingStatus
from base.notification import Notification
from base.base_hire import BaseNotificationManager, BaseReportManager
class BookingManagment(BaseNotificationManager, BaseReportManager):    
    @property
    def booked(self) -> int:
        return BookingStatus.BOOKED.value
    @property
    def canceled(self) -> int:
        return BookingStatus.CANCELED.value
    @property
    def pended(self) -> int:
        return BookingStatus.PENDING.value
    
    @property
    def name(self) -> str:
        return f'Booking({self.vechile.name} for customer {self.customer.name}'
    
    def create_booking(self, start_date, end_date, vechile, customer, invoice=None) -> object:
        self.customer = customer
        self.vechile = vechile
        self.vechile.booking_status = self.pended
        self.start_date = start_date
        self.end_date = end_date
        self.invoice = invoice
        return self
    
    def confirm(self) -> bool:
        """to book a vechile"""
        # TODO: searching in database from start_date and end_date to check if car booked or not in this time
        if self.invoice and self.vechile.booking_status != self.booked:
            self.vechile.booking_status = self.booked
            msg = f'Booking done succsessfully'
            self._send_notification(msg=msg, obj=self.customer)
            return True
        return False
        
    def cancel(self) -> bool:
        """to cancel booking """
        if self.booked:
            self.vechile.booking_status = self.canceled
            return True
        return False
        
        
    def reset_to_pending(self)-> bool:
        """Reset booking state to pending"""
        self.vechile.booking_status = self.pended
        return True
        