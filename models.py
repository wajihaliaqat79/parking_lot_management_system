from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Vehicle:
    plate: str
    vehicle_type: str

@dataclass
class Spot:
    spot_id: str
    vehicle_type: str
    occupied: bool = False
    ticket_id: Optional[str] = None

@dataclass
class Ticket:
    ticket_id: str
    plate: str
    vehicle_type: str
    spot_ids: list[str]
    entry_time: datetime
    exit_time: Optional[datetime] = None
    fee: Optional[float] = None

    @property
    def active(self) -> bool:
        return self.exit_time is None

@dataclass
class Visit:
    ticket_id: str
    plate: str
    vehicle_type: str
    spot_ids: list[str]
    entry_time: datetime
    exit_time: datetime
    duration_minutes: int
    fee: float



    