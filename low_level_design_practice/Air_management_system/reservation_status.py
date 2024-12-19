from enum import Enum

class ReservationStatus(Enum):
    BOOKED = 1
    CANCELLED = 2
    REFUNDED = 3