# This file shall contain the performance tests for the floydwarshall function to determine,
# if the non-functional requirements are fulfilled.

# At first the floydwarshall function and the test graphs will be imported.
# The big testing graph with 20x20 matrix will be tested in a separate unit.
from Floydwarshall.function import floydwarshall
from test_cases import test_graph_a
from test_cases import test_graph_b
from test_cases import test_graph_d

# The next import is the cProfile
# which is the common profile to get a test report on how often and how fast programs run.
import cProfile

# With sys and os the code imports the essential libraries to update the path to the folders of test cases.
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

floydwarshall(test_graph_a)
floydwarshall(test_graph_b)
floydwarshall(test_graph_d)

# The following lines will perform the actual tests to evaluate the performance of the floydwarshall function.
if __name__ == "__main__":
    cProfile.run("floydwarshall(test_graph_a)")
    cProfile.run("floydwarshall(test_graph_b)")
    cProfile.run("floydwarshall(test_graph_d)")
