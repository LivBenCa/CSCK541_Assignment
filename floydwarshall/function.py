# This function shall use recursive methodology to apply the Floyd-Warshall Algorithm.

def floydwarshall(dist):
    # The variable 'v' shall determine how many nodes the graph passed by dist has
    v = len(dist)

    # The function 'searchminimum' shall contain three different variables 'i, j, k'.
    # The variable 'i' stands for the starting node; the variable 'j' stands for the ending node.
    # The variable 'k' stands for the intermediate nodes.
    def searchminimum(i, j, k):

        # When there are no intermediate nodes,
        # the starting and ending node will have the minimum value as distance and therefore be returned.
        # Since the recursive function subtracts 1 from the base case in the following code,
        # 'k' shall be -1 to return the base case.
        if k == -1:
            return dist[i][j]

        # For each other number for 'k' (e.g. 3, 2, 1, ...)
        # the count of nodes decreases with the recursive function by 1 for each loop, starting with 'v'.
        # The recursive function also compares the distance between starting node/ending node
        # and the addition of starting node/intermediate node +  ending node/intermediate node to find the minimum.
        else:
            return min(searchminimum(i, j, k-1), searchminimum(i, k, k-1) + searchminimum(k, j, k-1))

    # The following for-loop finds the smallest shortestpath() result by looping in the range from 0 to 'v'.
    # It also updates the graph and overwrites given distances with shorter ones.
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = searchminimum(i, j, k)
    return dist
