from datetime import datetime
import urllib.error, urllib.request
from outage import Outage, OutageState


class InternetConnectionStatusChecker:

    def __init__(self) -> None:
        self.ongoing_outage = False

    @staticmethod
    def is_outage() -> bool:
        try:
            r = urllib.request.Request("https://www.google.com", method="HEAD")
            urllib.request.urlopen(r, timeout=2)
        except (
            urllib.error.URLError,
            urllib.error.HTTPError,
            urllib.error.ContentTooShortError):
            return True
        else:
            return False

    def check_connection(self) -> Outage:
        if self.is_outage():
            # ongoing outage
            if self.ongoing_outage:
                return Outage(OutageState.ONGOING)
            
            print('New outage!')
            self.ongoing_outage = True
            return Outage(OutageState.NEW)

        # there was no outage
        if not self.ongoing_outage:
            return Outage(OutageState.NONE)
        
        # end current outage
        if self.ongoing_outage:
            print('Outage ended')
            self.ongoing_outage = False
            return Outage(OutageState.ENDED)
