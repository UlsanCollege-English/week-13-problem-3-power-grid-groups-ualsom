

def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # Build adjacency map for all given stations (include isolated stations)
    adj = {s: set() for s in stations}

    # Add undirected edges for each line, but only between known stations
    for a, b in lines:
        if a in adj and b in adj:
            adj[a].add(b)
            adj[b].add(a)

    visited = set()

    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj.get(node, ()):  # safe fallback
                if neigh not in visited:
                    stack.append(neigh)

    groups = 0
    for s in stations:
        if s not in visited:
            dfs(s)
            groups += 1

    return groups


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
