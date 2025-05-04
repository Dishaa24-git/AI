def prim(num_vertices, graph):
    in_mst = [False] * num_vertices  # Track which vertices are in the MST
    key = [float('inf')] * num_vertices  # Minimum weight edge for each vertex
    parent = [-1] * num_vertices  # To store the MST structure (parent-child relationship)
    
    key[0] = 0  # Start from vertex 0, set its key to 0 to include it in the MST
    
    for _ in range(num_vertices):
        min_key = float('inf')
        u = -1
        for v in range(num_vertices):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        
        in_mst[u] = True  # Include vertex 
        
        for v in range(num_vertices):
            if graph[u][v] != 0 and not in_mst[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    mst_edges = []
    for v in range(1, num_vertices):
        mst_edges.append((parent[v], v, graph[parent[v]][v]))
    return mst_edges


def get_graph_input():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = [[0] * num_vertices for _ in range(num_vertices)]     # Initialize the adjacency matrix 
    
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (u, v, weight) for each edge:")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        graph[u][v] = weight
        graph[v][u] = weight  
    return num_vertices, graph

if __name__ == "__main__":
    num_vertices, graph = get_graph_input()
    mst_edges = prim(num_vertices, graph)

    print("\nMinimum Spanning Tree (MST) edges:")
    total_weight = 0
    for u, v, weight in mst_edges:
        print(f"Edge ({u}, {v}) with weight {weight}")
        total_weight += weight
    
    print(f"\nTotal weight of the MST: {total_weight}")
    
