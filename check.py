import argparse
from datetime import datetime
import sys
import time

from internet_connection_checker import InternetConnectionStatusChecker
from report_file import ReportFile


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='Internet Outage Checker',
        description='Monitoring your internet connection outages. Saves outage duration to CSV file.',
        epilog='All arguments are optional')

    parser.add_argument('-i', '--interval', 
                        type=int, 
                        default=5, 
                        help='interval to check connection (send HEAD request) in seconds (default: 5)')

    parser.add_argument('-p', '--report_path', 
                        default='./internet_outage.csv', 
                        help="file path of status report file (default: './internet_outage.csv')")

    args = parser.parse_args()


    print(f'started at: {datetime.now().strftime("%d.%m.%Y")} ', end='')
    print(f'{datetime.now().strftime("%H:%M:%S")}')
    print(f'checking interval: every {args.interval} second(s)')

    report = ReportFile(path=args.report_path)
    internet = InternetConnectionStatusChecker(report_file=report)


    while True:
        try:
            internet.check_connection()
            time.sleep(args.interval)
        except KeyboardInterrupt:
            print("'K, bye!")
            sys.exit(0)
