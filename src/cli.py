import os
import click
from src.service import parser
from src.validator import input_validator


class Context:
    def __init__(self, expression: str):
        self.parser = parser.Parser(expression)


@click.command()
@click.argument("expression", type=str, required=True)
@click.pass_context
def cli(ctx, expression):
    if not input_validator.is_valid(expression):
        click.echo('Please add a valid cron expression')
        return

    ctx.obj = Context(expression)

    click.echo(ctx.obj.parser.parse_expression())

