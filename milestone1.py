
    
    
import json
import numpy as np


with open('C:/Input data/level0.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])


matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

def tsp(distance):
    n = len(distance)
    unvisited = set(range(1, n))
    current = 0
    path = [current]
    while unvisited:
        next_node = min(unvisited, key=lambda x: distance[current][x])
        path.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    path.append(0)
    return sum(distance[path[i]][path[i+1]] for i in range(n)), path

min_distance, path = tsp(matrix.tolist())


node_names = ['r0'] + [f'n{i}' for i in range(20)]
formatted_path = {
    'v0': {
        'path': [node_names[node] for node in path]
    }
}


print("Minimum distance for TSP:", min_distance)
print("Path:", formatted_path)


with open('level0_output.json', 'w') as outfile:
    json.dump(formatted_path, outfile, indent=4)
