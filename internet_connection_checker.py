from datetime import datetime
import urllib.error, urllib.request

from report_file import ReportFile


class InternetConnectionStatusChecker:

    def __init__(self, report_file: ReportFile) -> None:
        self.report = report_file
        self.was_outage = False

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

    def check_connection(self) -> bool:
        if self.is_outage():
            # ongoing outage
            if self.was_outage:
                return self.was_outage
            
            print('New outage!')
            outage_start_time = datetime.now()
            self.report.write(
                _date=outage_start_time.strftime("%d.%m.%Y"),
                _time=outage_start_time.strftime("%H:%M:%S"),
                event='OUTAGE START')
            self.was_outage = True

        # no outage
        else:
            # there was no outage
            if not self.was_outage:
                return self.was_outage
            
            # end current outage
            if self.was_outage:
                print('Outage ended')
                self.was_outage = False
                outage_end_time = datetime.now()

                self.report.write(
                    _date=outage_end_time.strftime("%d.%m.%Y"),
                    _time=outage_end_time.strftime("%H:%M:%S"),
                    event='OUTAGE END')
                return self.was_outage
