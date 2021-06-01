import pytest
from src import cli
from click.testing import CliRunner
from src.config import ERROR_INVALID_ARGUMENT
from columnar import columnar


@pytest.fixture
def runner():
    return CliRunner()


def get_columnar(minute, hour, day, month, week, command):
    data = [
        ['minute', minute],
        ['hour', hour],
        ['day of month', day],
        ['month', month],
        ['day of week', week],
        ['command', command]
    ]

    table = columnar(data, no_borders=True)

    return str(table)


@pytest.mark.parametrize(('argument', 'output'), [
    pytest.param('*/15 0 1,15 * 1-5 /usr/bin/find',
        get_columnar('0 15 30 45', '0', '1 15', '1 2 3 4 5 6 7 8 9 10 11 12', '1 2 3 4 5', '/usr/bin/find'),
        id='Valid with all standard cron format'),

    pytest.param('*/15    0 1,15 *           1-5                /usr/bin/find',
        get_columnar('0 15 30 45', '0', '1 15', '1 2 3 4 5 6 7 8 9 10 11 12', '1 2 3 4 5', '/usr/bin/find'),
        id='Valid with all standard cron format with spaces'),

    pytest.param('* * * * * /jarvis/do/this',
        get_columnar('0 1 2 3 4 5 6 7 8 9 10 11 12 13', '0 1 2 3 4 5 6 7 8 9 10 11 12 13',
            '1 2 3 4 5 6 7 8 9 10 11 12 13 14', '1 2 3 4 5 6 7 8 9 10 11 12', '0 1 2 3 4 5 6', '/jarvis/do/this'),
        id='All *'),

    pytest.param('0 0 1 1 0 /jarvis/do/this', get_columnar('0', '0', '1', '1', '0',
        '/jarvis/do/this'), id='Specific values'),

])
def test_returns_cron_parsed(runner, argument, output):
    result = runner.invoke(cli.cli, [argument])
    assert result.exit_code == 0
    assert ' '.join(result.output.split()) == ' '.join(output.split())


@pytest.mark.parametrize(('argument', 'output'), [
    pytest.param('*/15 0 1,15 * 1- /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Wrong range'),
    pytest.param('* * * * *', ERROR_INVALID_ARGUMENT, id='Missing command'),
    pytest.param('*/ * * * * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Wrong step'),
    pytest.param('*/150 * * * * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Step out of range'),
    pytest.param('*/5 * * * 1,7 /usr/bin/find', ERROR_INVALID_ARGUMENT, id='List out of range'),
    pytest.param('*/5 0 * * 1, /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Wrong list'),
    pytest.param('* /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Wrong cron'),
    pytest.param('* * * * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Wrong cron'),
    pytest.param('* * * B * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Wrong cron'),
    pytest.param('60 * * * * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Minute out of range'),
    pytest.param('* 24 * * * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Hour out of range'),
    pytest.param('* * 32 * * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Day out of range'),
    pytest.param('* * * 13 * /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Month out of range'),
    pytest.param('* * * * 7 /usr/bin/find', ERROR_INVALID_ARGUMENT, id='Week out of range')
])
def test_returns_invalid_cron_arguments(runner, argument, output):
    result = runner.invoke(cli.cli, [argument])
    assert result.exit_code == 0
    assert result.output.strip() == output