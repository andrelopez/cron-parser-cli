from croniter import croniter


class Parser:
    def __init__(self, expression: str):
        self.expression = expression
        self.minute, self.hour, self.day, self.month,\
            self.week, self.command = self.expression.split(maxsplit=5)




