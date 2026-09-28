def find_paths(graph, start, destination, n):
    paths = []

    def dfs(node, visited):
        # Destination reached
        if node == destination:
            # Destination ko mask me include nahi karenge,
            # kyunki dono scouts destination share kar sakte hain.
            paths.append(visited & ~(1 << destination))
            return

        for next_node in graph[node]:
            # Same town dobara visit nahi karna
            if visited & (1 << next_node):
                continue

            dfs(next_node, visited | (1 << next_node))

    dfs(start, 1 << start)
    return paths


# Number of towns and roads
n, m = map(int, input().split())

# Graph
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    # Convert 1-based town number to 0-based index
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)


# Starting towns of two scouts
start1, start2 = map(int, input().split())
start1 -= 1
start2 -= 1

# Outpost
destination = int(input()) - 1


# Find all possible simple paths
paths1 = find_paths(graph, start1, destination, n)
paths2 = find_paths(graph, start2, destination, n)


answer = float('inf')

# Compare both scouts' paths
for path1 in paths1:
    for path2 in paths2:

        # Paths must not have any common town.
        # Destination was already removed from both masks,
        # so destination can be shared.
        if path1 & path2:
            continue

        total_towns = (path1 | path2).bit_count() + 1

        answer = min(answer, total_towns)


if answer == float('inf'):
    print("Impossible")
else:
    print(answer)