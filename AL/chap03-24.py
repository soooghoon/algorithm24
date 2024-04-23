def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        nbr = graph[start] - visited
        for v in sorted(nbr):
            dfs(graph, v, visited)


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D']),
    'C': set(['A','D', 'E']),
    'D': set(['B','C','F']),
    'E': set(['C','G', 'H']),
    'F': set(['D']),
    'G': set(['E','H']),
    'H': set(['E', 'G'])
}


dfs(graph, 'A')