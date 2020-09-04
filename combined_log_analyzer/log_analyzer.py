import sys
import datetime


def log_parser(log_line: str):
    log_list: list = log_line.strip().split(" ")
    host_name: str = log_list[0]
    request_time: str = log_list[3].replace("[", "") + log_list[4].replace("]", "")
    date_time = datetime.datetime.strptime(request_time, "%d/%b/%Y:%H:%M:%S%z")

    return (host_name, date_time)


def sort_accesses(accesses):
    return sorted(accesses.items(), key=lambda x: x[1], reverse=True)


def log_analyzer(date_from: str, to_date: str):
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
    }

    iso_date_from = datetime.datetime.fromisoformat(date_from)
    iso_to_date = datetime.datetime.fromisoformat(to_date)

    for log_line in sys.stdin:
        host_name, date_time = log_parser(log_line)

        if iso_date_from <= date_time <= iso_to_date:
            if host_name in remote_host_accesses:
                remote_host_accesses[host_name] += 1
            else:
                remote_host_accesses[host_name] = 1

            each_hour_accesses[str(date_time.hour).zfill(2)] += 1

    return (sort_accesses(remote_host_accesses), each_hour_accesses)
