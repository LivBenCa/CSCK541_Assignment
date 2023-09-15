from Recursive import floyd_input
from test_cases import (test_1, output_1)

import unittest


class TestFloyd(unittest.TestCase):
    def test_graph_1(self):
        self.assertEqual(floyd_input(test_1), output_1, 'failed')


if __name__ == '__main__':

    unittest.main()
