# Floyd Warshall Algorithm in python,


# The number of vertices
nV = 6

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 2, 1, 5, INF, INF],
     [2, 0, 2, 3, INF, INF],
     [1, 2, 0, 3, 1, INF],
     [5, 3, 3, 0, 1, 5],
     [INF, INF, INF, 1, 0, 1],
     [INF, INF, INF, 5, 1, 0]]

floyd_warshall(G)