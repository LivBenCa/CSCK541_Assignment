import unittest

from Functions.Recursive import floyd_input
from graph_tests import (graph_test_1, result_distance_1)
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class FloydTest(unittest.TestCase):
    def GraphTest_1(self):
        self.assertEqual(floyd_input(graph_test_1), result_distance_1, "Error")


if __name__ == '__main__':

    unittest.main()
