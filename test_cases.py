import sys

NO_PATH = sys.maxsize
# The file test_cases.py contains different graphs to test the stability of the functions
# in the file Recursive.py

test_1 = [[0, 5, NO_PATH, 10],
          [NO_PATH, 0, 3, NO_PATH],
          [NO_PATH, NO_PATH, 0, 1],
          [NO_PATH, NO_PATH, NO_PATH, 0]]

output_1 = [[0, 5, 8, 9],
            [NO_PATH, 0, 3, 4],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]]
