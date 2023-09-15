# This file contains test graphs to be implemented into the test unit and apply the 'searchminimum' function.
# The paths of each matrix that do not exist or are unknown, shall be assumed as infinite, using the infinite function.
INF = float('inf')

# The first matrix shall be the test graph from the pdf of the module CSCK541-Mid-Module assignment.
test_graph_a = [[0, 7, INF, 8],
                [INF, 0, 5, INF],
                [INF, INF, 0, 2],
                [INF, INF, INF, 0]]

result_a = [[0, 7, 12, 8],
            [INF, 0, 5, 7],
            [INF, INF, 0, 2],
            [INF, INF, INF, 0]]

# The second matrix is to play around with bigger intermediate values and test outside the comfort zone.
# The matrix was created with a software from the homepage of the TU Munich and represents distances
# between European cities.
test_graph_b = [[0, INF, INF, INF, INF, 343, INF, 1435, 464, INF],
                [INF, 0, INF, INF, INF, 879, 954, 811, INF, 524],
                [INF, INF, 0, INF, 1364, 1054, INF, INF, INF, INF],
                [INF, INF, INF, 0, INF, INF, 433, INF, INF, 1053],
                [INF, INF, 1364, INF, 0, 1106, INF, INF, INF, 766],
                [343, 879, 1054, INF, 1106, 0, INF, INF, INF, INF],
                [INF, 954, INF, 433, INF, INF, 0, 837, INF, INF],
                [1435, 811, INF, INF, INF, INF, 837, 0, INF, INF],
                [464, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                [INF, 524, INF, 1053, 766, INF, INF, INF, INF, 0]]

result_b = [[0, 1222, 1397, 2609, 1449, 343, 2176, 1435, 464, 1746],
            [1222, 0, 1933, 1387, 1290, 879, 954, 811, 1686, 524],
            [1397, 1933, 0, 3183, 1364, 1054, 2887, 2744, 1861, 2130],
            [2609, 1387, 3183, 0, 1819, 2266, 433, 1270, 3073, 1053],
            [1449, 1290, 1364, 1819, 0, 1106, 2244, 2101, 1913, 766],
            [343, 879, 1054, 2266, 1106, 0, 1833, 1690, 807, 1403],
            [2176, 954, 2887, 433, 2244, 1833, 0, 837, 1899, 1335],
            [1435, 811, 2744, 1270, 2101, 1690, 837, 0, 1899, 1335],
            [464, 1686, 1861, 3073, 1913, 807, 2640, 1899, 0, 2210],
            [1746, 524, 2130, 1053, 766, 1403, 1478, 1335, 2210, 0]]

# The third matrix is to test the limits of the stack space by calling a bigger amount unresolved functions.
test_graph_c = [[0, 8, INF, INF, 5, 3, INF, INF, 5, 2, 8, 11, 23, 17, 1, 2],
                [INF, 0, INF, 11, 5, INF, 9, INF, INF, 4, INF, 1, 4, 11, INF, 8],
                [7, 4, 0, INF, INF, 4, INF, INF, 5, 3, INF, INF, 5, 2, 8, 11],
                [4, 4, 8, 0, 1, INF, INF, 2, INF, INF, INF, INF, INF, INF, INF, 3],
                [4, 4, 8, INF, 0, INF, INF, INF, INF, 4, INF, 11, 5, INF, 9, INF],
                [4, 4, 8, INF, INF, 0, INF, INF, 7, 4, 9, INF, INF, 4, INF, INF],
                [4, 4, 8, 3, INF, 2, 0, 12, INF, INF, INF, INF, INF, INF, INF, 12],
                [4, 4, 8, INF, INF, INF, INF, 0, 5, 2, 9, 22, 3, 7, 9, 1],
                [2, 8, 8, INF, 5, 3, INF, INF, 0, 2, 8, 11, 23, 17, 1, 2],
                [INF, 5, INF, 11, 5, INF, 9, INF, INF, 0, INF, 1, 4, 11, INF, 8],
                [7, 4, 2, INF, INF, 4, INF, INF, 5, 3, 0, INF, 5, 2, 8, 11],
                [INF, 7, 4, INF, 1, 2, 9, 2, INF, INF, INF, 0, INF, INF, INF, 3],
                [INF, 7, 4, 11, 2, INF, INF, 3, 5, 4, INF, 11, 0, INF, 9, INF],
                [INF, 7, 4, INF, INF, 9, INF, INF, 7, 4, 9, INF, INF, 0, INF, INF],
                [INF, 7, 4, 3, INF, INF, 8, 12, INF, 6, INF, INF, INF, INF, 0, 12],
                [INF, 7, 4, INF, INF, INF, INF, 1, 5, 2, INF, 22, 3, 7, 9, 0]]
