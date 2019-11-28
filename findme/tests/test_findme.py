from unittest import TestCase

from click.testing import CliRunner

from findme import __version__, _cli


def findme(*args):
    return CliRunner().invoke(_cli.main, args)


class TestFindMe(TestCase):
    def test_it_finds_stuff(self):
        result = findme("integers", "x", "x>10")
        self.assertTrue(int(result.output) > 10)

    def test_version(self):
        result = findme("--version")
        self.assertIn(__version__, result.output)
