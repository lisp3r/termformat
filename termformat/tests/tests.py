from subprocess import check_output
import unittest

from termformat import format_snake


class TestFormatter(unittest.TestCase):

    def setUp(self):
        self.formatter = format_snake.Formatter()
        self.text = 'Hello, World!'
        self.formatter(self.text)

    def testBg(self):
        color = '#FAA500'
        string = self.formatter.bg(color).bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = f'\x1b[;48;2;250;165;0m{self.text}\x1b[0m\n'
        self.assertEqual(result, expected)

    def testFg(self):
        color = '#FAA500'
        string = self.formatter.fg(color).bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = f'\x1b[;38;2;250;165;0m{self.text}\x1b[0m\n'
        self.assertEqual(result, expected)

    def testBold(self):
        string = self.formatter.bold().bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = f'\x1b[;1m{self.text}\x1b[0m\n'
        self.assertEqual(result, expected)

    def testDim(self):
        string = self.formatter.dim().bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = f'\x1b[;2m{self.text}\x1b[0m\n'
        self.assertEqual(result, expected)

    def testFlush1(self):
        self.formatter.bg('#FAA500').bake()
        string = self.formatter.fg('#FAA500').bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = f'\x1b[;38;2;250;165;0m{self.text}\x1b[0m\n'
        self.assertEqual(result, expected)

    def testFlush2(self):
        self.formatter.bg('#FAA500').bake()
        string = self.formatter('Another string').fg('#FAA500').bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = '\x1b[;38;2;250;165;0mAnother string\x1b[0m\n'
        self.assertEqual(result, expected)

    def testFormatChain(self):
        string = self.formatter('Chain is cool!').bg('#9dc1e3').bold().fg('#1b8148').bake()
        result = check_output(['echo', string]).decode('ascii')
        expected = '\x1b[;48;2;157;193;227;1;38;2;27;129;72mChain is cool!\x1b[0m\n'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
