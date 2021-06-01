from src.config import MAX_COLUMNS, MINUTE, HOUR, DAY, WEEK, MONTH, ALLOWED_VALUES,\
    CHAR_ALL, CHAR_STEP, CHAR_RANGE, CHAR_LIST
from src.utils import utils


class Parser:
    def __init__(self, expression: str):
        self.expression = expression
        self._minute, self._hour, self._day, self._month,\
            self._week, self._cmd = self.expression.split(maxsplit=5)

    def parse_expression(self) -> str:
        args = {
            'minute': self._format_special_char(MINUTE, self._minute),
            'hour': self._format_special_char(HOUR, self._hour),
            'day': self._format_special_char(DAY, self._day),
            'month': self._format_special_char(MONTH, self._month),
            'week': self._format_special_char(WEEK, self._week),
            'cmd': self._cmd
        }

        return utils.print_table(**args)

    def _format_special_char(self, _type: str, val: str):
        res = val
        if val == CHAR_ALL:
            res = self._get_all_allowed_values(_type)
        elif CHAR_STEP in val:
            res = self._get_step_values(_type, self._get_step(val))
        elif CHAR_LIST in val:
            res = self._get_list_values(val)
        elif CHAR_RANGE in val:
            res = self._get_range_values(val)

        return res

    def _get_all_allowed_values(self, _type: str) -> str:
        range_values = ALLOWED_VALUES[_type]
        start, end = range_values
        result = [val for val in range(start, end + 1)]

        return self._row_output(result)

    def _get_step_values(self, _type: str, step: int) -> str:
        range_values = ALLOWED_VALUES[_type]
        result = []
        start, end = range_values
        total = start
        while total < end:
            result.append(total)
            total += step

        return self._row_output(result)

    def _get_list_values(self, _list: str) -> str:
        result = _list.split(CHAR_LIST)

        return self._row_output(result)

    def _get_range_values(self, _list: str) -> str:
        start, end = _list.split(CHAR_RANGE)
        result = [val for val in range(int(start), int(end) + 1)]

        return self._row_output(result)

    def _get_step(self, arg: str) -> int:
        return int(arg.split(CHAR_STEP)[1])

    def _row_output(self, array: list) -> str:
        size = MAX_COLUMNS if len(array) > MAX_COLUMNS else len(array)

        return " ".join([str(array[i]) for i in range(size)])