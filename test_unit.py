# This test unit shall be the environment for the test graphs a-c from the file test_cases
# and determine if the floyd funtion from the file 'function' fulfills the functional requirements.

# At first the floyd function and the test graphs will be imported.
# The big testing graph with 20x20 matrix will be tested in a separate unit.
from Floydwarshall.function import floydwarshall
from test_cases import (test_graph_a, test_graph_b, test_graph_d,
                        result_a, result_b, result_d)

# The next steps import the essential libraries to run the tests and update the path for the folders.
import unittest
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class TestFloyd(unittest.TestCase):

    def test_floyd_a(self):
        self.assertEqual(floydwarshall(test_graph_a), result_a, False)

    def test_floyd_b(self):
        self.assertEqual(floydwarshall(test_graph_b), result_b, False)

    def test_floyd_d(self):
        self.assertEqual(floydwarshall(test_graph_d), result_d, False)


if __name__ == '__main__':
    unittest.main()
