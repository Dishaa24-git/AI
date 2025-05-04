class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, color, node, c):
        # Check if any adjacent vertex has the same color
        for neighbor in self.graph[node]:
            if color[neighbor] == c:
                return False
        return True

    def graph_coloring_util(self, color, node, m):
        # If all vertices are assigned a color then return True
        if node == self.V:
            return True

        # Consider this node and try different colors
        for c in range(1, m+1):
            # Check if assignment of color c to node is possible
            if self.is_safe(color, node, c):
                color[node] = c
                # Recur to assign colors to the rest of the vertices
                if self.graph_coloring_util(color, node + 1, m):
                    return True
                # Backtrack if assigning color c doesn't lead to a solution
                color[node] = 0

        # If no color can be assigned to this vertex then return False
        return False

    def solve_graph_coloring(self, m):
        # Initialize color assignment for all vertices
        color = [0] * self.V

        # Start coloring from the first vertex
        if not self.graph_coloring_util(color, 0, m):
            print("Solution does not exist.")
            return False
        
        # Print the solution
        print("Solution found:")
        self.print_solution(color)
        return True

    def print_solution(self, color):
        print("Vertex : Color")
        for node in range(self.V):
            print(f" {node} : {color[node]}")

def main():
    # Example input
    V = int(input("Enter the number of vertices: "))
    graph = Graph(V)

    # Add edges to the graph (since it's an undirected graph)
    E = int(input(f"Enter the number of edges: "))
    print("Enter the edges (u, v) where u and v are vertex numbers:")
    for _ in range(E):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    
    # Get the number of colors
    m = int(input("Enter the number of colors: "))
    
    # Try to solve the graph coloring problem
    if not graph.solve_graph_coloring(m):
        print("No solution with the given number of colors.")

if __name__ == "__main__":
    main()

