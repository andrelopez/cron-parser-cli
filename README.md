# Cron Parser Cli
It will transform standard cron expressions into a human-readable cron table.

## Usage
Use the following command:
`cron-parser CRON-EXPRESSION`

The output will be formatted as a table with a maximum of 14 values

For example, the following input argument:

```bash
~$ cron-parser ＂*/15 0 1,15 * 1-5 /usr/bin/find＂
```

It will return the following output:

```bash
minute        0 15 30 45 
hour          0
day of month  1 2 3 4 5 6 7 8 9 10 11 12
month         1 15
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Development

Create a new Python 3 environment called venv and activate it (Mac or Linux):

```bash
~$ python3 -m venv ./venv
~$ source ./venv/bin/activate
~$ (venv) pip install --editable .
```

### Run Tests

Tests are managed by [pytest](https://docs.pytest.org/en/6.2.x/contents.html) and tests are under `test` directory
You can run the tests with the following command:

```bash
~$ (venv) pytest tests -v   
```
