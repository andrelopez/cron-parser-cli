from cron_validator import CronValidator


def is_valid(expression: str) -> bool:
    if not expression:
        return False

    input = expression.split()

    if len(input) < 6:
        return False

    try:
        CronValidator.parse(" ".join(input[:5]))
    except ValueError as e:
        print(f"Error: {str(e)}")
        return False

    return True