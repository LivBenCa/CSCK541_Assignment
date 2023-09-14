import sys

NO_PATH = sys.maxsize
# The file graph_tests.py contains different graphs to test the stability of the functions
# in the file Recursive.py

graph_test_1 = [[0, 5, NO_PATH, 10],
                [NO_PATH, 0, 3, NO_PATH],
                [NO_PATH, NO_PATH, 0, 1],
                [NO_PATH, NO_PATH, NO_PATH, 0]]

result_distance_1 = [[0, 5, 8, 10],
                     [NO_PATH, 0, 3, 4],
                     [NO_PATH, NO_PATH, 0, 1],
                     [NO_PATH, NO_PATH, NO_PATH, 0]]
