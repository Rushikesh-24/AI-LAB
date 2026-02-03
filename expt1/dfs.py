def dfs(graph, start):
    n = len(graph)
    visited = [False] * n
    stack = [start]
    dfs_order = []
    
    print(f"Starting DFS from node {start}")
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            dfs_order.append(node)
            print(f"Visiting node: {node}")
            
            for neighbor in range(n-1, -1, -1):
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
                    print(f"Adding node {neighbor} to stack")
    
    return dfs_order

def main():
    n = int(input("Enter the number of nodes: "))
    
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    start_node = 0
    
    
    print("PERFORMING DFS TRAVERSAL")
    print(f"{'='*50}")
    
    result = dfs(graph, start_node)
    
    
    print("DFS TRAVERSAL COMPLETED")
    print(f"DFS Order: {result}")

if __name__ == "__main__":
    main()
