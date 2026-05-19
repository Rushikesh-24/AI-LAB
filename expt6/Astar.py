from heapq import heappush, heappop

def astar(graph, h, start, goal):
    open_heap = []
    open_map = {}    
    closed_map = {}  

    g_start = 0
    f_start = g_start + h[start]
    start_item = (start, "null", h[start], g_start, f_start)

    heappush(open_heap, (f_start, start))
    open_map[start] = start_item

    print(f"{'OPEN':<60} | {'CLOSED'}")
    print("-" * 100)

    while open_heap:
        sorted_open_nodes = sorted(open_map.values(), key=lambda item: item[4])

        open_str = ", ".join([str(v) for v in sorted_open_nodes])
        closed_str = ", ".join([str(v) for v in closed_map.values()]) if closed_map else "()"
        print(f"{open_str:<60} | {closed_str}")

        _, current = heappop(open_heap)

        if current not in open_map:
            continue

        item = open_map.pop(current)
        closed_map[current] = item

        if current == goal:
            path = []
            temp = goal
            
            _, _, _, final_cost, _ = closed_map[goal]
            
            while temp != "null":
                n, p, _, _, _ = closed_map[temp]
                path.append(n)
                temp = p
            path.reverse()
            return path, final_cost

        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_map:
                continue

            new_g = item[3] + cost
            new_h = h[neighbor]
            new_f = new_g + new_h

            if neighbor not in open_map or new_g < open_map[neighbor][3]:
                open_map[neighbor] = (neighbor, current, new_h, new_g, new_f)
                heappush(open_heap, (new_f, neighbor))

    return None, float("inf")


if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 5), ('E', 12)],
        'C': [('F', 2)],
        'D': [('G', 3)],
        'E': [('G', 4)],
        'F': [('G', 2)],
        'G': []
    }

    h = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 3,
        'E': 6,
        'F': 1,
        'G': 0
    }

    path, cost = astar(graph, h, 'A', 'G')
    print("\nGoal State Found")
    print("\nPATH :", path)
    print("COST :", cost)