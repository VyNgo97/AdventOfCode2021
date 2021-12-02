from unittest import TestCase
import unittest
from main import *

example_data = ['forward 5',
                'down 5',
                'forward 8',
                'up 3',
                'down 8',
                'forward 2']

class Test(TestCase):

    def test_part1(self):
        self.assertEqual(150, p1(example_data))

    def test_part2(self):
        self.assertEqual(900, p2(example_data))

if __name__ == '__main__':
    unittest.main()