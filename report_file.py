import csv
from pathlib import Path


class ReportFile:

    CSV_COLUMNS = ["DATE", "TIME", "EVENT"]

    def __init__(self, path: str) -> None:
        self.REPORT_FILE_PATH = path
        self.create_if_not_exists()

    def create_if_not_exists(self) -> None:
        report_file = Path(self.REPORT_FILE_PATH)
        file_exists = report_file.exists()

        if not file_exists:
            Path(self.REPORT_FILE_PATH).touch(exist_ok=False)

            with open(self.REPORT_FILE_PATH,
                      "w",
                      encoding="utf-8",
                      newline='') as csvfile:
                writer = csv.DictWriter(
                    csvfile,
                    fieldnames=self.CSV_COLUMNS,
                    quoting=csv.QUOTE_ALL)
                writer.writeheader()
        print(f'Report file: {self.REPORT_FILE_PATH}')

    def write(self, _date, _time, event) -> None:
        with open(self.REPORT_FILE_PATH,
                  "a+",
                  encoding="utf-8",
                  newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=self.CSV_COLUMNS,
                quoting=csv.QUOTE_ALL,
            )
            writer.writerow({
                self.CSV_COLUMNS[0]: _date,
                self.CSV_COLUMNS[1]: _time,
                self.CSV_COLUMNS[2]: event})
