def add_edge(graph, u, v):
    graph.setdefault(u, []).append(v)   #checks if key exists, if not default val returned
    graph.setdefault(v, []).append(u)

def dfs(graph, node, visited):  #node
    print(node, end=" ")
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, nodes, visited): #nodes
    if not nodes:  
        return
    
    next_level = []
    for node in nodes:
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    next_level.append(neighbor)
    
    bfs(graph, next_level, visited)

def main():
    graph = {}
    n = int(input("Enter number of edges: "))
    for _ in range(n):
        u, v = map(int, input().split())
        add_edge(graph, u, v)
    
    print("\nADJACENCY LIST:")
    for vertex in graph:
        print(f"{vertex}: {graph[vertex]}")
    
    start_node = int(input("\nEnter the start node: "))
    
    print("\nDFS:")
    dfs(graph, start_node, set())

    print("\nBFS:")
    bfs(graph, [start_node], set()) #[start_node]

if __name__ == "__main__":
    main()

