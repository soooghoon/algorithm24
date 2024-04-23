import queue

def bfs(graph, start):
    visited = {start}  
    que = queue.Queue()  
    que.put(start) 

    while not que.empty():  
        v = que.get()  
        print(v, end=' ')  
    
        nbr = sorted(graph[v] - visited)
        for u in nbr:
            visited.add(u)  
            que.put(u)  

mygraph = {
   'A': set(['B', 'C']),
    'B': set(['A', 'D']),
    'C': set(['A','D', 'E']),
    'D': set(['B','C','F']),
    'E': set(['C','G', 'H']),
    'F': set(['D']),
    'G': set(['E','H']),
    'H': set(['E', 'G'])
}

print('BFS: ', end="")
bfs(mygraph, 'A')
