import typer
import datetime
from .log_analyzer import log_analyzer


def total_result_display(
    date_from: str = typer.Option(
        "start",
        "-f",
        "--from",
        help="Starting point of the period for aggregation."
        + "The format must be an ISO 8601 extension.",
        show_default=False,
    ),
    to_date: str = typer.Option(
        "now",
        "-t",
        "--to",
        help="End point of the period for aggregation."
        + "The format must be an ISO 8601 extension.",
        show_default=False,
    ),
    time_zone: str = typer.Option(
        "+09:00",
        "-z",
        "--zone",
        help="Time zone for the period of aggregation."
        + "The format must be an ISO 8601 extension.",
        show_default=True,
    ),
):
    """Receives Apache http server log from standard input and parses the log.
    The number of accesses for each host name and the number of accesses for each time
    are output to standard output as a result.
    We supply the target period and time zone with option arguments.
    """

    is_from_arg: bool = date_from != "start"
    is_to_arg: bool = to_date != "now"

    if is_from_arg:
        try:
            iso_date_from = datetime.datetime.fromisoformat(date_from)
        except ValueError:
            typer.echo("error")
            return
    else:
        iso_date_from = datetime.datetime.min

    if is_to_arg:
        try:
            iso_to_date = datetime.datetime.fromisoformat(to_date)
        except ValueError:
            typer.echo("error3")
            return
    else:
        iso_to_date = datetime.datetime.max

    remote_host_accesses, hour_accesses = log_analyzer(
        iso_date_from.strftime("%Y-%m-%d %H:%M:%S") + time_zone,
        iso_to_date.strftime("%Y-%m-%d %H:%M:%S") + time_zone,
    )

    typer.echo("Number of accesses by remote host")
    for remote_host in remote_host_accesses:
        typer.echo(remote_host[0] + str(remote_host[1]).rjust(15))

    typer.echo("\n\nNumber of accesses by hour")
    for hour, accesses in hour_accesses.items():
        typer.echo(hour + str(accesses).rjust(21))


def main():
    typer.run(total_result_display)
