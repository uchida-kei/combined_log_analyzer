import datetime
from combined_log_analyzer import __version__
from combined_log_analyzer.log_analyzer import sort_accesses, log_parser


def test_version():
    assert __version__ == "0.0.1"


def test_log_parser():
    host, date = log_parser(
        '10.2.3.5 - - [18/Apr/2015:00:10:47 +0900] "GET / HTTP/1.1" 200 854 "-" '
        + '"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)"'
    )
    assert host == "10.2.3.5"
    assert date == datetime.datetime(
        2015, 4, 18, 0, 10, 47, tzinfo=datetime.timezone(datetime.timedelta(hours=9))
    )


def test_sort_accesses():
    accesses = {"10.2.3.4": 15, "10.2.3.5": 12, "10.2.3.6": 20, "10.2.3.7": 9}
    assert sort_accesses(accesses) == [
        ("10.2.3.6", 20),
        ("10.2.3.4", 15),
        ("10.2.3.5", 12),
        ("10.2.3.7", 9),
    ]
