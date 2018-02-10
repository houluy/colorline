from unittest import TestCase

from colorline import cprint

class TestEnd(TestCase):
    def test_end(self):
        cprint('test newline', end='')
        print('newline')
