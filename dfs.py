graph={
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','F'],
    'D' : ['B'],
    'E' : ['B','F'],
    'F' : ['C','E'],
}

visited=set()

def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)
            
dfs('A')

