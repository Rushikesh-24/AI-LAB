from collections import deque
from math import gcd


class State:
	def __init__(self, jug1, jug2, parent=None, action=""):
		self.jug1 = jug1
		self.jug2 = jug2
		self.parent = parent
		self.action = action

	def __eq__(self, other):
		return self.jug1 == other.jug1 and self.jug2 == other.jug2

	def __hash__(self):
		return hash((self.jug1, self.jug2))

	def __str__(self):
		return f"({self.jug1},{self.jug2})"


def is_valid_state(state, jug1_capacity, jug2_capacity):
	"""Check if a state is within jug capacities."""
	return 0 <= state.jug1 <= jug1_capacity and 0 <= state.jug2 <= jug2_capacity


def get_successors(state, jug1_capacity, jug2_capacity):
	"""Generate all valid successor states."""
	successors = []

	# Fill jug 1
	successors.append(State(jug1_capacity, state.jug2, state, f"Fill Jug 1 ({jug1_capacity}L)"))

	# Fill jug 2
	successors.append(State(state.jug1, jug2_capacity, state, f"Fill Jug 2 ({jug2_capacity}L)"))

	# Empty jug 1
	successors.append(State(0, state.jug2, state, "Empty Jug 1"))

	# Empty jug 2
	successors.append(State(state.jug1, 0, state, "Empty Jug 2"))

	# Pour jug 1 -> jug 2
	transfer_1_to_2 = min(state.jug1, jug2_capacity - state.jug2)
	successors.append(
		State(
			state.jug1 - transfer_1_to_2,
			state.jug2 + transfer_1_to_2,
			state,
			f"Pour {transfer_1_to_2}L from Jug 1 to Jug 2"
		)
	)

	# Pour jug 2 -> jug 1
	transfer_2_to_1 = min(state.jug2, jug1_capacity - state.jug1)
	successors.append(
		State(
			state.jug1 + transfer_2_to_1,
			state.jug2 - transfer_2_to_1,
			state,
			f"Pour {transfer_2_to_1}L from Jug 2 to Jug 1"
		)
	)

	# Keep only valid, non-identical states
	unique_successors = []
	seen = set()
	for successor in successors:
		if successor != state and is_valid_state(successor, jug1_capacity, jug2_capacity):
			if successor not in seen:
				seen.add(successor)
				unique_successors.append(successor)

	return unique_successors


def solve_water_jug(jug1_capacity, jug2_capacity, target):
	"""Solve the water jug problem using BFS."""
	initial_state = State(0, 0)

	queue = deque([initial_state])
	visited = {initial_state}
	traversal_order = []

	print("\n=== TRAVERSAL TREE ===\n")
	print("Starting state:", initial_state)
	traversal_order.append(initial_state)

	while queue:
		current_state = queue.popleft()

		# Goal: target liters in either jug
		if current_state.jug1 == target or current_state.jug2 == target:
			print("\n=== GOAL REACHED ===\n")
			return current_state, traversal_order

		successors = get_successors(current_state, jug1_capacity, jug2_capacity)

		for successor in successors:
			if successor not in visited:
				visited.add(successor)
				queue.append(successor)
				traversal_order.append(successor)
				print(f"  From {current_state} -> {successor} [{successor.action}]")

	print("\n=== NO SOLUTION FOUND ===\n")
	return None, traversal_order


def print_solution_path(goal_state):
	"""Print solution path from initial state to goal."""
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
	print("WATER JUG PROBLEM")
	print("=" * 50)
	print()

	jug1_capacity = int(input("Enter Jug 1 capacity (in liters): "))
	jug2_capacity = int(input("Enter Jug 2 capacity (in liters): "))
	target = int(input("Enter target amount (in liters): "))

	if jug1_capacity <= 0 or jug2_capacity <= 0:
		print("Jug capacities must be positive integers.")
		return

	if target < 0:
		print("Target amount cannot be negative.")
		return

	print(f"\nSolving for Jug 1 = {jug1_capacity}L, Jug 2 = {jug2_capacity}L, Target = {target}L")
	print("State format: (jug1_amount, jug2_amount)")

	if target == 0:
		print("\nTarget is 0L. Already at goal state (0,0).")
		return

	if target > max(jug1_capacity, jug2_capacity):
		print("No solution exists! Target is greater than both jug capacities.")
		return

	if target % gcd(jug1_capacity, jug2_capacity) != 0:
		print("No solution exists! Target is not divisible by gcd of jug capacities.")
		return

	goal_state, traversal_order = solve_water_jug(jug1_capacity, jug2_capacity, target)

	if goal_state:
		print_solution_path(goal_state)
		print(f"Total states explored: {len(traversal_order)}")
	else:
		print("No solution exists for this configuration!")


if __name__ == "__main__":
	main()
