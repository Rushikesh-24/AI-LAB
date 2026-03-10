from collections import deque

class State:
    def __init__(self, missionaries_left, cannibals_left, boat_position, parent=None, action=""):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_position = boat_position  # 'l' for left, 'r' for right
        self.parent = parent
        self.action = action
    
    def __eq__(self, other):
        return (self.missionaries_left == other.missionaries_left and 
                self.cannibals_left == other.cannibals_left and 
                self.boat_position == other.boat_position)
    
    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_position))
    
    def __str__(self):
        return f"({self.missionaries_left},{self.cannibals_left},{self.boat_position})"

def is_valid_state(state, total_missionaries, total_cannibals):
    """Check if a state is valid"""
    m_left = state.missionaries_left
    c_left = state.cannibals_left
    m_right = total_missionaries - m_left
    c_right = total_cannibals - c_left
    
    # Check bounds
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    
    # Check if cannibals outnumber missionaries on either side
    # (missionaries can be 0, but if not, they must be >= cannibals)
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    
    return True

def get_successors(state, total_missionaries, total_cannibals, boat_capacity):
    """Generate all valid successor states"""
    successors = []
    
    # Generate all possible moves (m missionaries, c cannibals)
    # where 1 <= m + c <= boat_capacity
    for m in range(boat_capacity + 1):
        for c in range(boat_capacity + 1):
            if 1 <= m + c <= boat_capacity:
                if state.boat_position == 'l':
                    # Moving from left to right
                    new_state = State(
                        state.missionaries_left - m,
                        state.cannibals_left - c,
                        'r',
                        state,
                        f"Move {m}M, {c}C from L to R"
                    )
                else:
                    # Moving from right to left
                    new_state = State(
                        state.missionaries_left + m,
                        state.cannibals_left + c,
                        'l',
                        state,
                        f"Move {m}M, {c}C from R to L"
                    )
                
                if is_valid_state(new_state, total_missionaries, total_cannibals):
                    successors.append(new_state)
    
    return successors

def solve_missionaries_cannibals(num_missionaries, num_cannibals, boat_capacity):
    """Solve the missionaries and cannibals problem using BFS"""
    
    # Initial state: all on left side
    initial_state = State(num_missionaries, num_cannibals, 'l')
    
    # Goal state: all on right side
    goal_state = State(0, 0, 'r')
    
    # BFS
    queue = deque([initial_state])
    visited = {initial_state}
    traversal_order = []  # To track the order of exploration
    
    print("\n=== TRAVERSAL TREE ===\n")
    print("Starting state:", initial_state)
    traversal_order.append(initial_state)
    
    while queue:
        current_state = queue.popleft()
        
        # Check if goal reached
        if current_state == goal_state:
            print("\n=== GOAL REACHED ===\n")
            return current_state, traversal_order
        
        # Generate successors
        successors = get_successors(current_state, num_missionaries, num_cannibals, boat_capacity)
        
        for successor in successors:
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)
                traversal_order.append(successor)
                print(f"  From {current_state} -> {successor} [{successor.action}]")
    
    print("\n=== NO SOLUTION FOUND ===\n")
    return None, traversal_order

def print_solution_path(goal_state):
    """Print the solution path from initial to goal state"""
    path = []
    current = goal_state
    
    while current is not None:
        path.append(current)
        current = current.parent
    
    path.reverse()
    
    print("\n=== SOLUTION PATH ===\n")
    print(f"Steps required: {len(path) - 1}\n")
    
    for i, state in enumerate(path):
        if i == 0:
            print(f"Step {i}: {state} [Initial State]")
        else:
            print(f"Step {i}: {state} [{state.action}]")
    
    print()

def main():
    print("=" * 50)
    print("MISSIONARIES AND CANNIBALS PROBLEM")
    print("=" * 50)
    print()
    
    num_missionaries = int(input("Enter the number of missionaries: "))
    num_cannibals = int(input("Enter the number of cannibals: "))
    boat_capacity = int(input("Enter the boat capacity (max people): "))
    
    print(f"\nSolving for {num_missionaries} missionaries, {num_cannibals} cannibals, boat capacity: {boat_capacity}")
    print("State format: (missionaries_left, cannibals_left, boat_position)")
    print("  - missionaries_left: number of missionaries on left bank")
    print("  - cannibals_left: number of cannibals on left bank")
    print("  - boat_position: 'l' for left bank, 'r' for right bank")
    
    # Solve the problem
    goal_state, traversal_order = solve_missionaries_cannibals(num_missionaries, num_cannibals, boat_capacity)
    
    if goal_state:
        print_solution_path(goal_state)
        print(f"Total states explored: {len(traversal_order)}")
    else:
        print("No solution exists for this configuration!")

if __name__ == "__main__":
    main()
