import urllib.error, urllib.request
from outage import Outage, OutageState


class InternetConnectionStatusChecker:

    def __init__(self) -> None:
        self.ongoing_outage = False

    @staticmethod
    def _is_outage() -> bool:
        try:
            r = urllib.request.Request("https://www.google.com", method="HEAD")
            urllib.request.urlopen(r, timeout=2)
        except (
            urllib.error.URLError,
            urllib.error.HTTPError,
            urllib.error.ContentTooShortError,
            TimeoutError
        ):
            return True
        else:
            return False

    def check_outage(self) -> Outage:
        if self._is_outage():
            if self.ongoing_outage:
                return Outage(OutageState.ONGOING)

            print('New outage!')
            self.ongoing_outage = True
            return Outage(OutageState.NEW)

        # no outage but ongoing is True
        # so end current outage
        if self.ongoing_outage:
            print('Outage ended')
            self.ongoing_outage = False
            return Outage(OutageState.ENDED)

        # no outage
        return Outage(OutageState.NONE)
