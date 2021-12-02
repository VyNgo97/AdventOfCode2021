from unittest import TestCase
import unittest
from main import *

example_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

class Test(TestCase):

    def test_part1(self):
        self.assertEqual(7, find_count_p1(example_data))

    def test_part2(self):
        self.assertEqual(5, find_count_p2(example_data))

if __name__ == '__main__':
    unittest.main()