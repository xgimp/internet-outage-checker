from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OutageState(Enum):
    NONE = "None"
    NEW = "New Outage"
    ONGOING = "Ongoing"
    ENDED = "Outage Ended"


@dataclass
class Outage:
    state: OutageState
    date: datetime = datetime.now()

    def __post_init__(self):
        # set actual datetime
        # without this time of init will be set 
        # in all instances of this class
        self.date = datetime.now()
