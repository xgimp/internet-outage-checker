import csv
from pathlib import Path


class ReportFile:

    CSV_COLUMNS = ["DATE", "TIME", "EVENT"]

    def __init__(self, path: str) -> None:
        self.REPORT_FILE_PATH = Path(path)
        self.create_if_not_exists()

    def create_if_not_exists(self) -> None:
        print(f'Report file: {self.REPORT_FILE_PATH.resolve()}')
        
        if self.REPORT_FILE_PATH.exists():
            return None
    
        self.REPORT_FILE_PATH.touch(exist_ok=False)
        with open(self.REPORT_FILE_PATH,
                  "w",
                  encoding="utf-8",
                  newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=self.CSV_COLUMNS,
                quoting=csv.QUOTE_ALL)
            writer.writeheader()

    def write(self, _date, _time, event) -> None:
        CSV_HEADER = {
            self.CSV_COLUMNS[0]: _date,
            self.CSV_COLUMNS[1]: _time,
            self.CSV_COLUMNS[2]: event
        }
        with open(self.REPORT_FILE_PATH,
                  "a+",
                  encoding="utf-8",
                  newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=self.CSV_COLUMNS,
                quoting=csv.QUOTE_ALL)
            writer.writerow(CSV_HEADER)
