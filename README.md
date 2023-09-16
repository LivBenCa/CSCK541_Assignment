# CSCK541_Assignment
# Recursive Floyd-Warshall Algorithm
> The algorithm finds the shortest distance between all nodes of a graph with variable size by using recursion.

## Installation
Use the package manager pip to install the package.
```bash
pip install Floydwarshall
```

Use the package manager pip to install the dependencies.
```bash
pip install -r requirements.txt
```

## Usage example
Import the function to your script:
```python
from floydwarshall.function import floydWarshall

# The paths of each input matrix that do not exist or are unknown, shall be assumed as infinite, using the infinite function.
INF = float('inf')

# Example input:

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

# Expected output:

result_b = [[0, 1222, 1397, 2609, 1449, 343, 2176, 1435, 464, 1746],
            [1222, 0, 1933, 1387, 1290, 879, 954, 811, 1686, 524],
            [1397, 1933, 0, 3183, 1364, 1054, 2887, 2744, 1861, 2130],
            [2609, 1387, 3183, 0, 1819, 2266, 433, 1270, 3073, 1053],
            [1449, 1290, 1364, 1819, 0, 1106, 2244, 2101, 1913, 766],
            [343, 879, 1054, 2266, 1106, 0, 1833, 1690, 807, 1403],
            [2176, 954, 2887, 433, 2244, 1833, 0, 837, 2640, 1478],
            [1435, 811, 2744, 1270, 2101, 1690, 837, 0, 1899, 1335],
            [464, 1686, 1861, 3073, 1913, 807, 2640, 1899, 0, 2210],
            [1746, 524, 2130, 1053, 766, 1403, 1478, 1335, 2210, 0]]


## Runnning Unit Tests
To run the unit tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python -m unittest test_cases.py
```


## Runnning Performance Tests
To run the performance tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python -m cProfile test_cases.py
```

## Contributing

1. Fork it (<https://github.com/LivBenCa/CSCK541_Assignment/fork>)
2. Create your feature branch 
3. Commit your changes 
4. Push to the branch 
5. Create a new Pull Request
