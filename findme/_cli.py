import click

from hypothesis import find, strategies

from findme import __version__


def _predicate_from_str(stredicate):
    code = compile(stredicate, "<findme>", "eval")
    print code.co_names
    return eval("lambda {}: {}".format(stredicate))


def _strategy_from_str(stringtergy):
    return getattr(strategies, stringtergy)()


@click.command(context_settings=dict(help_option_names=["--help", "-h"]))
@click.argument("strategy", type=_strategy_from_str)
@click.argument("predicate")
@click.version_option(prog_name="findme", version=__version__)
def main(strategy, predicate):
    click.echo(
        repr(find(strategy, _predicate_from_str(predicate))),
    )
