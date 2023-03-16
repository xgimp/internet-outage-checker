# About 

Simple script for monitoring internet outages. It creates CSV file that contain outage duration.

## Requirements:
* Python 3.6 or newer


### run the script
Clone this repository and run 

```
python app.py
```

## Usage

```
usage: Outage Checker [-h] [-i INTERVAL] [-p REPORT_PATH]

Monitoring your internet connection outages. Saves outage duration to CSV file.

options:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        interval to check connection (send HEAD request) in seconds (default: 5)
  -p REPORT_PATH, --report_path REPORT_PATH
                        file path of status report file (default: './internet_outage.csv')      

All arguments are optional
```
