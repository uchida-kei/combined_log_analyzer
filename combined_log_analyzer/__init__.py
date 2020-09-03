__version__ = "0.1.0"

import sys
import datetime

remote_host_accesses = {}
each_hour_accesses = {
    "00": 0,
    "01": 0,
    "02": 0,
    "03": 0,
    "04": 0,
    "05": 0,
    "06": 0,
    "07": 0,
    "08": 0,
    "09": 0,
    "10": 0,
    "11": 0,
    "12": 0,
    "13": 0,
    "14": 0,
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0,
    "21": 0,
    "22": 0,
    "23": 0,
    "24": 0,
}


def log_parser(log_line: str):
    log_list: list = log_line.strip().split(" ")
    host_name: str = log_list[0]
    request_time: str = log_list[3].replace("[", "") + log_list[4].replace("]", "")
    date_time = datetime.datetime.strptime(request_time, "%d/%b/%Y:%H:%M:%S%z")

    return (host_name, date_time)


for log_line in sys.stdin:
    host_name, date_time = log_parser(log_line)
    if host_name in remote_host_accesses:
        remote_host_accesses[host_name] += 1
    else:
        remote_host_accesses[host_name] = 1

    each_hour_accesses[str(date_time.hour).zfill(2)] += 1

sorted_remote_host_accesses = sorted(
    remote_host_accesses.items(), key=lambda x: x[1], reverse=True
)

print("Number of accesses by remote host")
for remote_host in sorted_remote_host_accesses:
    print(remote_host[0] + str(remote_host[1]).rjust(15))

print("\n")

print("Number of accesses by hour")
for hour, hour_accesses in each_hour_accesses.items():
    print(hour + str(hour_accesses).rjust(21))
