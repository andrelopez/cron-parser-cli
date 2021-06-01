from columnar import columnar


def print_table(minute: str, hour: str, day: str, month: str, week: str, cmd: str) -> str:
    table = [
        ['minute', minute],
        ['hour', hour],
        ['day of month', day],
        ['month', month],
        ['day of week', week],
        ['command', cmd]
    ]
    table = columnar(table, no_borders=True)

    return str(table)