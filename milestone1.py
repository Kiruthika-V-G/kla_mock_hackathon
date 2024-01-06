


'''import json
import numpy as np

# Load data from JSON file
with open('C:/Input data/level0.json') as f:
    data = json.load(f)

# Extract neighbourhood distance and distances between neighbourhoods
neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])

# Combine neighbourhood_distance and neighbourhoods into a 2D array
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Print the matrix
lst = matrix.tolist()
print("Matrix:")
print(lst)

# Define the TSP function
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

# Solve the TSP problem
min_distance, path = tsp(matrix.tolist())

# Print the solution
#print("Minimum distance for TSP:", min_distance)
#print("Path:", path)

formatted_path = {
    "v0": {
        "path": ["r0"] + ["n" + str(node) for node in path[1:-1]] + ["r0"]
    }
}

# Print the solution
print("Minimum distance for TSP:", min_distance)
print("Path:", formatted_path)

json_object = json.dumps(formatted_path, indent=4)
 
# Writing to sample.json
with open("level0_output.json", "w") as out:
    out.write(json_object)'''
    
    
import json
import numpy as np

# Load data from JSON file
with open('C:/Input data/level0.json') as f:
    data = json.load(f)

# Extract neighbourhood distance and distances between neighbourhoods
neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])

# Combine neighbourhood_distance and neighbourhoods into a 2D array
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Define the TSP function
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

# Solve the TSP problem
min_distance, path = tsp(matrix.tolist())

# Format the path with node names
node_names = ['r0'] + [f'n{i}' for i in range(20)]
formatted_path = {
    'v0': {
        'path': [node_names[node] for node in path]
    }
}

# Print the solution
print("Minimum distance for TSP:", min_distance)
print("Path:", formatted_path)

# Write the solution to a JSON file
with open('level0_output.json', 'w') as outfile:
    json.dump(formatted_path, outfile, indent=4)