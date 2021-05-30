# Cron Parser Cli
The cron string will be passed to your application as a single argument.

`~$ cron-parser ＂*/15 0 1,15 * 1-5 /usr/bin/find＂`

The output should be formatted as a table with the field name taking the first 14 columns and

the times as a space-separated list following it.
For example, the following input argument:

`*/15 0 1,15 * 1-5 /usr/bin/find`

It will return the following:

|   |   |
|---|---|
| minute  | 0 15 30 45  |
|  hour |   0 |
|  day of month |  1 2 3 4 5 6 7 8 9 10 11 12 |
|  month |  1 15 |
|  day of week |  1 2 3 4 5 |
|  command |  /usr/bin/find |

## Install

Create a new Python 3 environment called venv and activate it (Mac or Linux):

```buildoutcfg
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip install --editable .
```

