from unittest import TestCase

from click.testing import CliRunner

from findme import __version__, _cli


def findme(*args):
    return CliRunner().invoke(_cli.main, args, catch_exceptions=False)



class TestFindMe(TestCase):
    def succeed(self, *args):
        result = findme(*args)
        self.assertEqual(result.exit_code, 0)
        return result.output

    def test_it_finds_stuff(self):
        import pudb; pu.db
        output = self.succeed("integers", "x>10")
        self.assertTrue(int(output) > 10)

    def test_version(self):
        output = self.succeed("--version")
        self.assertIn(__version__, output)
