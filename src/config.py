# SPECIAL CHARACTERS
CHAR_ALL = '*'
CHAR_LIST = ','
CHAR_RANGE = '-'
CHAR_STEP = '*/'

# Types
MINUTE = 'minute'
HOUR = 'hour'
DAY = 'day'
MONTH = 'month'
WEEK = 'week'

# ALLOWED VALUES
ALLOWED_VALUES = {
    MINUTE: (0, 59),
    HOUR: (0, 23),
    DAY: (1, 31),
    MONTH: (1, 12),
    WEEK: (0, 6)
}

# DEFAULTS
MAX_COLUMNS = 14