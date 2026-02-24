def dfs(graph, start, goal):
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    stack = [start]
    dfs_order = []
    
    print(f"Starting DFS from node {start} to {goal}\n")
    
    while stack:
        open_nodes = list(stack)
        closed_nodes = [i for i in range(n) if visited[i]]
        
        open_list = []
        for node in open_nodes:
            p = parent[node] if parent[node] != -1 else 'NU'
            open_list.append(f"({node},{p},{node})")
        
        closed_list = []
        for node in closed_nodes:
            p = parent[node] if parent[node] != -1 else 'NU'
            closed_list.append(f"({node},{p},{node})")
        open_str = "".join(open_list) if open_list else "(empty)"
        closed_str = "".join(closed_list) if closed_list else "(empty)"
        
        space_between = max(60 - len(open_str), 5)
        print(f"{open_str}{' ' * space_between}{closed_str}")
        print()
        
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            dfs_order.append(node)
            
            if node == goal:
                print(f"Goal node {goal} found!\n")
                path = []
                current = goal
                while current != -1:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return dfs_order, path
            
            for neighbor in range(n-1, -1, -1):
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    parent[neighbor] = node
                    stack.append(neighbor)
    
    return dfs_order, []

def main():
    n = int(input("Enter the number of nodes: "))
    
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    start_node = int(input("Enter starting node: "))
    goal_node = int(input("Enter goal node: "))
    
    print("\nPERFORMING DFS TRAVERSAL")
    print(f"{'='*50}")
    
    dfs_order, path = dfs(graph, start_node, goal_node)
    
    print("\nDFS TRAVERSAL COMPLETED")
    if path:
        path_str = ' -> '.join(map(str, path))
        length = len(path) - 1  # Number of edges
        print(f"\nPath: {path_str}     Length = {length} ({len(path)} steps)")
    else:
        print(f"No path found from {start_node} to {goal_node}")

if __name__ == "__main__":
    main()
