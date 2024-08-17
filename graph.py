from collections import defaultdict, deque


def create_graph(n, connections):
    graph = defaultdict(list)
    for i in range(n):
        person, neighbors = connections[i].split('#')
        neighbors = neighbors.split('-')
        graph[person].extend(neighbors)
    return graph


def bfs(graph, start, target):
    queue = deque([start])
    visited = set()

    while queue:
        current = queue.popleft()
        if current == target:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False


n = int(input())
connections = []
for _ in range(n):
    connections.append(input())

start, target = input().split('-')
graph = create_graph(n, connections)

result = bfs(graph, start, target)

print(result)