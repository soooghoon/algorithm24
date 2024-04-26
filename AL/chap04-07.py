def dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def topological_sort_dfs(graph):
    visited = set()
    stack = []
    
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)
    return stack[::-1]


mygraph = {
    'A': ['D', 'E', 'B'],
    'B': ['E', 'F', 'C'],
    'C': ['G'],
    'D': ['E'],
    'E': [],
    'F': ['G'],
    'G': ['H'],
    'H': []
}
topological_order_dfs = topological_sort_dfs(mygraph)
print('DFS Topological Sort:', ' '.join(topological_order_dfs)) 