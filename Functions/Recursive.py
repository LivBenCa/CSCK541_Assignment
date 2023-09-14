import sys
NO_PATH = sys.maxsize


def floyd_input(graph):

    max_length = len(graph[0])

    def recursion_floyd(start_node, end_node, intermediate):
        if intermediate == 0:
            return graph[start_node][end_node]
        else:
            return min(recursion_floyd(start_node, end_node, intermediate - 1),
                       recursion_floyd(start_node, intermediate, intermediate - 1) +
                       recursion_floyd(intermediate, end_node, intermediate - 1))

    for intermediate in range(max_length):
        for start_node in range(max_length):
            for end_node in range(max_length):
                graph[start_node][end_node] = recursion_floyd(start_node, end_node, intermediate)

        return graph
