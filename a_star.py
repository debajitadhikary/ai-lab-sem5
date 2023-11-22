import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(initial_state, goal_state, successors, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(initial_state, None, 0, heuristic(initial_state, goal_state))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            return construct_path(current_node)

        closed_set.add(current_node.state)

        for successor, cost in successors(current_node.state):
            if successor in closed_set:
                continue

            new_cost = current_node.cost + cost
            new_node = Node(successor, current_node, new_cost, heuristic(successor, goal_state))

            if not any(node.cost < new_node.cost and node.state == new_node.state for node in open_set):
                heapq.heappush(open_set, new_node)

    return None  # No path found

def construct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

# Example usage:
if __name__ == "__main__":
    # Define your initial state, goal state, successors function, and heuristic function.
    # For example:
    initial_state = (0, 0)


    goal_state = (2, 2)

    def successors(state):
        x, y = state
        return [((x+1, y), 1), ((x, y+1), 1)]

    def heuristic(state, goal_state):
        x1, y1 = state
        x2, y2 = goal_state
        return abs(x1 - x2) + abs(y1 - y2)

    path = astar_search(initial_state, goal_state, successors, heuristic)
    if path:
        print("\nA* Path:", path)
    else:
        print("No path found")

print("\n")