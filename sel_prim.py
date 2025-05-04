def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def prim(num_vertices, graph):
    in_mst = [False] * num_vertices
    key = [float('inf')] * num_vertices
    parent = [-1] * num_vertices

    key[0] = 0

    for _ in range(num_vertices):
        min_key = float('inf')
        u = -1
        for v in range(num_vertices):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        in_mst[u] = True

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
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (u, v, weight):")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        graph[u][v] = weight
        graph[v][u] = weight
    return num_vertices, graph

def menu():
    while True:
        print("\nMenu:")
        print("1. Selection Sort")
        print("2. Prim's Algorithm - Minimum Spanning Tree")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_str = input("Enter numbers separated by spaces: ")
            arr = list(map(int, input_str.split()))
            print("Original array:", arr)
            sorted_arr = selection_sort(arr)
            print("Sorted array:", sorted_arr)

        elif choice == '2':
            num_vertices, graph = get_graph_input()
            mst_edges = prim(num_vertices, graph)
            total_weight = 0
            print("\nMinimum Spanning Tree (MST) edges:")
            for u, v, weight in mst_edges:
                print(f"Edge ({u}, {v}) with weight {weight}")
                total_weight += weight
            print(f"Total weight of the MST: {total_weight}")

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()





"""Menu:
1. Selection Sort
2. Prim's Algorithm - Minimum Spanning Tree
3. Exit
Enter your choice (1/2/3): 1
Enter numbers separated by spaces: 8 67 4 23
Original array: [8, 67, 4, 23]
Sorted array: [4, 8, 23, 67]

Menu:
1. Selection Sort
2. Prim's Algorithm - Minimum Spanning Tree
3. Exit
Enter your choice (1/2/3): 2
Enter the number of vertices: 5
Enter the number of edges: 7
Enter the edges (u, v, weight):
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
3 4 9

Minimum Spanning Tree (MST) edges:
Edge (0, 1) with weight 2
Edge (1, 2) with weight 3
Edge (0, 3) with weight 6
Edge (1, 4) with weight 5
Total weight of the MST: 16

Menu:
1. Selection Sort
2. Prim's Algorithm - Minimum Spanning Tree
3. Exit
Enter your choice (1/2/3): 3
Exiting program.
"""