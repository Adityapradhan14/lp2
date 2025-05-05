graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']

node_colors = {}

for node in graph:
    for color in colors:
        if all(node_colors.get(neighbor) != color for neighbor in graph[node]):
            node_colors[node] = color
            break

print("Coloring:", node_colors)

