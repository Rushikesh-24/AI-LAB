import heapq

def best_first_search(graph, start, goal, heuristic_values):
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    priority_queue = [(heuristic_values[start], start)]
    search_order = []
    
    print(f"Starting Best First Search from node {start} to {goal}\n")
    
    while priority_queue:
        open_nodes = sorted(list(set([node for _, node in priority_queue])))
        closed_nodes = [i for i in range(n) if visited[i]]
        
        open_list = []
        for node in open_nodes:
            p = parent[node] if parent[node] != -1 else 'NU'
            open_list.append(f"({node},{p},{heuristic_values[node]:.0f})")
        
        closed_list = []
        for node in closed_nodes:
            p = parent[node] if parent[node] != -1 else 'NU'
            closed_list.append(f"({node},{p},{heuristic_values[node]:.0f})")
        
        open_str = "".join(open_list) if open_list else "(empty)"
        closed_str = "".join(closed_list) if closed_list else "(empty)"
        
        space_between = max(60 - len(open_str), 5)
        print(f"{open_str}{' ' * space_between}{closed_str}")
        print()
        
        value, node = heapq.heappop(priority_queue)
        
        if visited[node]:
            continue
            
        visited[node] = True
        search_order.append(node)
        
        if node == goal:
            print(f"Goal node {goal} found!\n")
            path = []
            current = goal
            while current != -1:
                path.append(current)
                current = parent[current]
            path.reverse()
            return search_order, path
        
        for neighbor in range(n):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                if parent[neighbor] == -1:
                    parent[neighbor] = node
                heapq.heappush(priority_queue, (heuristic_values[neighbor], neighbor))
    
    return search_order, []
def main():
    n = int(input("Enter the number of nodes: "))
    
    graph = []
    print("Enter adjacency matrix (one row per line, space-separated):")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    heuristic_values = []
    print("Enter heuristic values for each node (space-separated):")
    heuristic_values = list(map(float, input().split()))
    
    start_node = int(input("Enter starting node: "))
    goal_node = int(input("Enter goal node: "))
    
    print("\nPERFORMING BEST FIRST SEARCH TRAVERSAL")
    
    search_order, path = best_first_search(graph, start_node, goal_node, heuristic_values)
    
    print("\nBEST FIRST SEARCH TRAVERSAL COMPLETED")
    if path:
        path_str = ' -> '.join(map(str, path))
        length = len(path) - 1  # Number of edges
        print(f"\nPath: {path_str}     Length = {length} ({len(path)} steps)")
    else:
        print(f"No path found from {start_node} to {goal_node}")

if __name__ == "__main__":
    main()
