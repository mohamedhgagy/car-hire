from . import BookingStatus
class BookingManagment:    
    @property
    def booked(self) -> int:
        return BookingStatus.BOOKED.value
    @property
    def canceled(self) -> int:
        return BookingStatus.CANCELED.value
    @property
    def pended(self) -> int:
        return BookingStatus.PENDING.value
    
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
        if self.invoice:
            self.vechile.booking_status = self.booked
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
        
        
        
        