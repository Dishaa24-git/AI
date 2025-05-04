class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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
    edges.sort(key=lambda edge: edge[2])  # Sort by weight
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
    print("Enter the edges (u v weight):")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        edges.append((u, v, weight))

    return num_vertices, edges


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def main_menu():
    while True:
        print("\n===== MENU =====")
        print("1. Perform Selection Sort")
        print("2. Find MST using Kruskal's Algorithm")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_str = input("Enter numbers separated by spaces: ")
            arr = list(map(int, input_str.split()))
            print("Original array:", arr)
            sorted_arr = selection_sort(arr)
            print("Sorted array:", sorted_arr)

        elif choice == '2':
            num_vertices, edges = get_graph_input()
            mst = kruskal(num_vertices, edges)
            print("\nMinimum Spanning Tree (MST) edges:")
            total_weight = 0
            for u, v, weight in mst:
                print(f"({u}, {v}) with weight {weight}")
                total_weight += weight
            print(f"Total weight of the MST: {total_weight}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()


"""
Enter your choice (1/2/3): 2
Enter the number of vertices: 4
Enter the number of edges: 5
Enter the edges (u v weight):
0 1 3
0 2 6
2 3 1
1 3 8
1 2 4         

Minimum Spanning Tree (MST) edges:
(2, 3) with weight 1
(0, 1) with weight 3
(1, 2) with weight 4
Total weight of the MST: 8
"""