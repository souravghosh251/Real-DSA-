num_vertices = int(input("Enter number of vertices "))
num_edges = int(int(input("Enter number of edges ")))

adj_matrix = [[0]* num_vertices for row in range(num_vertices)]

for edge_index in range(num_edges):
    source_vertex,destination_vertex = map(int , input("Enter edge and vertices (u,v) : ").split())
    adj_matrix[source_vertex][destination_vertex] = 1
    adj_matrix[source_vertex][destination_vertex] =1

for row in adj_matrix:
    print(row)

