class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Rank is used for optimizing the union operation

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(num_vertices, edges):
    edges.sort(key=lambda edge: edge[2])    #sorting based on weight as weight is at 2nd index

    disjoint_set = DisjointSet(num_vertices)
    mst = []

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            disjoint_set.union(u, v)

    return mst

def get_graph_input():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    edges = []
    print("Enter the edges (u, v, weight) for each edge:")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        edges.append((u, v, weight))

    return num_vertices, edges

if __name__ == "__main__":
    num_vertices, edges = get_graph_input()

    mst = kruskal(num_vertices, edges)

    # Print the Minimum Spanning Tree
    print("\nMinimum Spanning Tree (MST) edges:")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")

