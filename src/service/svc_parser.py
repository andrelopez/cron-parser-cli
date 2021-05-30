class Parser:
    def __init__(self, expression: str):
        self.expression = expression

    def is_valid(self) -> bool:
        if not self.expression:
            return False

        return True