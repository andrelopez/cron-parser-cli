from croniter import croniter


def is_valid(expression: str) -> bool:
    if not expression:
        return False

    input = expression.split()

    if len(input) < 6:
        return False

    return croniter.is_valid(" ".join(input[:5]))