import click

from hypothesis import find, strategies

from findme import __version__


def _predicate_from_str(name, stredicate):
    return eval("lambda {}: {}".format(name, stredicate))


def _strategy_from_str(stringtergy):
    return getattr(strategies, stringtergy)()


@click.command(context_settings=dict(help_option_names=["--help", "-h"]))
@click.argument("strategy", type=_strategy_from_str)
@click.argument("name")
@click.argument("predicate")
@click.version_option(prog_name="findme", version=__version__)
def main(strategy, name, predicate):
    click.echo(
        repr(find(strategy, _predicate_from_str(name, predicate))),
    )
