def floyd_input(graph):

    max_length = len(graph)

    def recursion_floyd(start_node, end_node, intermediate):
        if intermediate == -1:
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
