import os
import click
from src.service import svc_parser


class Context:
    def __init__(self, expression: str):
        self.parser = svc_parser.Parser(expression)


@click.command()
@click.argument("expression", type=str, required=True)
@click.pass_context
def cli(ctx, expression):
    ctx.obj = Context(expression)

    if not ctx.obj.parser.is_valid():
        click.echo('Please add a valid cron expression')
        return

    click.echo(f'The subcommand {ctx.obj.parser.expression}')

