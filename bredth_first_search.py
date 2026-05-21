def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    
    queue = [('', 0, 0)]
    result = []
    
    while queue:
        print(queue)
        current, opens_used, closes_used = queue.pop(0)
        
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    
    return result
print(gen_parentheses(2))



#depth_first_search

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for neighbor in range(len(graph[node]) -1,-1, -1):
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited 







#N-queens algorithm

def dfs_n_queens(n):
    
    if n < 1:
        return []

    solutions = []

    def solve (current_state):
        if len (current_state) == n:
            solutions.append(list(current_state))

        for col in range (n):
            if is_valid(current_state, col):
                current_state.append(col)
                solve(current_state)
                current_state.pop()

    def is_valid(state, new_col):
        row = len(state)
        for r, c in enumerate(state):
            if c == new_col:
                return False

            if abs(c - new_col) == abs(r - row):
                return False

        return True
    solve([])
    return solutions                                    