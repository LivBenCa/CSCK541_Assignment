# This file shall test the floydwarshall function on its performance with big graphs.
from Floydwarshall.function import floydwarshall
from test_cases import test_graph_c
import cProfile

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

floydwarshall(test_graph_c)

if __name__ == "__main__":
    cProfile.run("floydwarshall(test_graph_a)")
