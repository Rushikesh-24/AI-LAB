from collections import deque

def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    bfs_order = []
    
    print(f"Starting BFS from node {start}")
    
    while queue:
        node = queue.popleft()
        bfs_order.append(node)
        print(f"Visiting node: {node}")
        for neighbor in range(n):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                print(f"Adding node {neighbor} to queue")
    
    return bfs_order

def main():
    n = int(input("Enter the number of nodes: "))
    
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    start_node=0
    
    print("PERFORMING BFS TRAVERSAL")
    
    result = bfs(graph, start_node)
    
    print("BFS TRAVERSAL COMPLETED")
    print(f"BFS Order: {result}")

if __name__ == "__main__":
    main()
