'''import json
import numpy as np

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

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])
max_capacity = data['vehicles']['v0']['capacity']


matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods


neighbourhoods_sorted = [n for _, n in sorted(zip(order, neighbourhoods), reverse=True)]


slots = []
remaining_capacity = max_capacity
#print(remaining_capacity)

#print(neighbourhoods_sorted)

current_slot = []
for neighbourhood in neighbourhoods_sorted:
    #print("neighbourhood : ",neighbourhood)
    #print("index : ",neighbourhoods.index(neighbourhood))
    #print("order : ",order[neighbourhoods.index(neighbourhood)])
    if remaining_capacity >= order[neighbourhoods.index(neighbourhood)]:
        current_slot.append(neighbourhood)
        remaining_capacity -= order[neighbourhoods.index(neighbourhood)]
    else:
        slots.append(current_slot)  
        current_slot = [neighbourhood]
        remaining_capacity = max_capacity - order[neighbourhoods.index(neighbourhood)]


slots.append(current_slot)
#print(slots[0])
#print(len(slots))

dist = 0
formatted_slots={}
for i in range(len(slots)):
    slot_distance,slot_path=tsp(slots[i])
    #slot_distance, slot_path = tsp(matrix[np.ix_(slots[i], slots[i])])
    print(slot_distance,slot_path)
    dist+=slot_distance
    formatted_slots[f"path{i+1}"] = ["r0"] + [f"n{node}" for node in slot_path[1:-1]] + ["r0"]
print(dist)
print(formatted_slots)
res={'v0':formatted_slots}
print(res)

with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)'''
    
'''import json
import numpy as np

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

def insert_neighborhood(slot, neighborhood, order, remaining_capacity):
    if remaining_capacity >= order[neighborhood]:
        slot.append(neighborhood)
        remaining_capacity -= order[neighborhood]
    return slot, remaining_capacity

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])

max_capacity = data['vehicles']['v0']['capacity']
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Initialize variables
slots = []
remaining_capacity = max_capacity
current_slot = []

# Sort neighborhoods based on order quantity
neighbourhoods_sorted = [n for _, n in sorted(zip(order, range(len(neighbourhoods))), reverse=True)]

# Greedy insertion algorithm
for neighborhood_index in neighbourhoods_sorted:
    current_slot, remaining_capacity = insert_neighborhood(current_slot, neighborhood_index, order, remaining_capacity)

    # Check if adding the neighborhood improves the current slot's total distance
    current_distance, _ = tsp(matrix[np.ix_([0] + current_slot + [0], [0] + current_slot + [0])])
    new_slot = current_slot + [neighborhood_index]
    new_distance, _ = tsp(matrix[np.ix_([0] + new_slot + [0], [0] + new_slot + [0])])

    if new_distance < current_distance:
        current_slot = new_slot

    if remaining_capacity == 0:
        slots.append(current_slot)
        current_slot = []
        remaining_capacity = max_capacity

# Handle the last slot
if current_slot:
    slots.append(current_slot)

# Calculate total distance and format output
dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)
formatted_slots = {f"path{i+1}": ["r0"] + [f"n{node}" for node in slot] + ["r0"] for i, slot in enumerate(slots)}

# Print results
print(dist)
print(formatted_slots)

# Save results to JSON file
res = {'v0': formatted_slots}
with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)
'''

'''
import json
import numpy as np

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

def insert_neighborhood(slot, neighborhood, order, remaining_capacity):
    if remaining_capacity >= order[neighborhood]:
        slot.append(neighborhood)
        remaining_capacity -= order[neighborhood]
    return slot, remaining_capacity

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])

max_capacity = data['vehicles']['v0']['capacity']
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Initialize variables
slots = []
remaining_capacity = max_capacity
current_slot = []

# Iterate through all nodes
for neighborhood_index in range(20):
    current_slot, remaining_capacity = insert_neighborhood(current_slot, neighborhood_index, order, remaining_capacity)

    # Check if adding the neighborhood improves the current slot's total distance
    current_distance, _ = tsp(matrix[np.ix_([0] + current_slot + [0], [0] + current_slot + [0])])
    new_slot = current_slot + [neighborhood_index]
    new_distance, _ = tsp(matrix[np.ix_([0] + new_slot + [0], [0] + new_slot + [0])])

    if new_distance < current_distance:
        current_slot = new_slot

    if remaining_capacity == 0 or neighborhood_index == 19:
        slots.append(current_slot)
        current_slot = []
        remaining_capacity = max_capacity

# Calculate total distance and format output
dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)
formatted_slots = {f"path{i+1}": ["r0"] + [f"n{node}" for node in slot] + ["r0"] for i, slot in enumerate(slots)}

# Print results
print(dist)
print(formatted_slots)

# Save results to JSON file
res = {'v0': formatted_slots}
with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)
'''

'''
import json
import numpy as np

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

def insert_neighborhood(slot, neighborhood, order, remaining_capacity, max_capacity):
    if remaining_capacity >= order[neighborhood]:
        slot.append(neighborhood)
        remaining_capacity -= order[neighborhood]
    return slot, remaining_capacity

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])

max_capacity = data['vehicles']['v0']['capacity']
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Initialize variables
slots = []
remaining_capacity = max_capacity
current_slot = []

# Iterate through all nodes
for neighborhood_index in range(20):
    current_slot, remaining_capacity = insert_neighborhood(current_slot, neighborhood_index, order, remaining_capacity, max_capacity)

    # Check if adding the neighborhood improves the current slot's total distance
    current_distance, _ = tsp(matrix[np.ix_([0] + current_slot + [0], [0] + current_slot + [0])])
    new_slot = current_slot + [neighborhood_index]
    new_distance, _ = tsp(matrix[np.ix_([0] + new_slot + [0], [0] + new_slot + [0])])

    # If adding the neighborhood exceeds capacity, start a new slot
    if remaining_capacity < 0 or new_distance > current_distance:
        slots.append(current_slot)
        current_slot = [neighborhood_index]
        remaining_capacity = max_capacity - order[neighborhood_index]

    if neighborhood_index == 19:
        slots.append(current_slot)

# Calculate total distance and format output
dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)
formatted_slots = {f"path{i+1}": ["r0"] + [f"n{node}" for node in slot] + ["r0"] for i, slot in enumerate(slots)}

# Print results
print(dist)
print(formatted_slots)

# Save results to JSON file
res = {'v0': formatted_slots}
with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)
'''

'''
import json
import numpy as np

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

def insert_neighborhood(slot, neighborhood, order, remaining_capacity, max_capacity):
    if remaining_capacity >= order[neighborhood]:
        slot.append(neighborhood)
        remaining_capacity -= order[neighborhood]
    return slot, remaining_capacity

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])

max_capacity = data['vehicles']['v0']['capacity']
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Initialize variables
slots = []
remaining_capacity = max_capacity
current_slot = []

# Iterate through all nodes
for neighborhood_index in range(20):
    current_slot, remaining_capacity = insert_neighborhood(current_slot, neighborhood_index, order, remaining_capacity, max_capacity)

    # Check if adding the neighborhood improves the current slot's total distance
    current_distance, _ = tsp(matrix[np.ix_([0] + current_slot + [0], [0] + current_slot + [0])])
    new_slot = current_slot + [neighborhood_index]
    new_distance, _ = tsp(matrix[np.ix_([0] + new_slot + [0], [0] + new_slot + [0])])

    # If adding the neighborhood exceeds capacity or all neighborhoods are traversed, start a new slot
    if remaining_capacity < 0 or new_distance > current_distance or neighborhood_index == 19:
        slots.append(current_slot)
        current_slot = []
        remaining_capacity = max_capacity

# Calculate total distance and format output
dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)
formatted_slots = {f"path{i+1}": ["r0"] + [f"n{node}" for node in slot] + ["r0"] for i, slot in enumerate(slots)}

# Print results
print(dist)
print(formatted_slots)

# Save results to JSON file
res = {'v0': formatted_slots}
with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)
'''
'''
import json
import numpy as np

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

def insert_neighborhood(slot, neighborhood, order, remaining_capacity, max_capacity):
    if remaining_capacity >= order[neighborhood]:
        slot.append(neighborhood)
        remaining_capacity -= order[neighborhood]
    return slot, remaining_capacity

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])

max_capacity = data['vehicles']['v0']['capacity']
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Initialize variables
slots = []
remaining_capacity = max_capacity
current_slot = []

# Iterate through all nodes
for neighborhood_index in range(20):
    current_slot, remaining_capacity = insert_neighborhood(current_slot, neighborhood_index, order, remaining_capacity, max_capacity)

    # Check if adding the neighborhood improves the current slot's total distance
    current_distance, _ = tsp(matrix[np.ix_([0] + current_slot + [0], [0] + current_slot + [0])])
    new_slot = current_slot + [neighborhood_index]
    new_distance, _ = tsp(matrix[np.ix_([0] + new_slot + [0], [0] + new_slot + [0])])

    # If adding the neighborhood exceeds capacity or all neighborhoods are traversed or total distance exceeds 13000, start a new slot
    if remaining_capacity < 0 or new_distance > current_distance or neighborhood_index == 19 or (dist + new_distance) > 13000:
        if current_slot:
            slots.append(current_slot)
            current_slot = []
            remaining_capacity = max_capacity

# Calculate total distance and format output
dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)
formatted_slots = {f"path{i+1}": ["r0"] + [f"n{node}" for node in slot] + ["r0"] for i, slot in enumerate(slots)}

# Print results
print(dist)
print(formatted_slots)

# Save results to JSON file
res = {'v0': formatted_slots}
with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)
'''
import json
import numpy as np

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

def insert_neighborhood(slot, neighborhood, order, remaining_capacity, max_capacity):
    if remaining_capacity >= order[neighborhood]:
        slot.append(neighborhood)
        remaining_capacity -= order[neighborhood]
    return slot, remaining_capacity

with open('C:/Input data/level1a.json') as f:
    data = json.load(f)

neighbourhood_distance = data['restaurants']['r0']['neighbourhood_distance']
neighbourhoods = []
order = []
for i in range(20):
    neighbourhoods.append(data['neighbourhoods']['n' + str(i)]['distances'])
    order.append(data['neighbourhoods']['n' + str(i)]['order_quantity'])

max_capacity = data['vehicles']['v0']['capacity']
matrix = np.zeros((21, 21))
matrix[0, 1:] = neighbourhood_distance
matrix[1:, 0] = neighbourhood_distance
matrix[1:, 1:] = neighbourhoods

# Find an initial solution using a greedy algorithm
slots = []
remaining_capacity = max_capacity
current_slot = []

# Sort neighborhoods based on order quantity
neighbourhoods_sorted = [n for _, n in sorted(zip(order, range(len(neighbourhoods))), reverse=True)]

for neighborhood_index in neighbourhoods_sorted:
    current_slot, remaining_capacity = insert_neighborhood(current_slot, neighborhood_index, order, remaining_capacity, max_capacity)
    if remaining_capacity == 0:
        slots.append(current_slot)
        current_slot = []
        remaining_capacity = max_capacity

# Calculate total distance and format output
dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)
formatted_slots = {f"path{i+1}": ["r0"] + [f"n{node}" for node in slot] + ["r0"] for i, slot in enumerate(slots)}

# Check if the total distance exceeds 13000 and iteratively refine the solution
while dist > 13000:
    # Find the slot with the largest total distance
    max_slot_index = max(range(len(slots)), key=lambda i: tsp(matrix[np.ix_([0] + slots[i] + [0], [0] + slots[i] + [0])])[0])
    
    # Move the node with the highest order quantity to the next slot
    max_node_index = slots[max_slot_index].index(max(slots[max_slot_index], key=lambda node: order[node]))
    moving_node = slots[max_slot_index].pop(max_node_index)
    slots[(max_slot_index + 1) % len(slots)].append(moving_node)
    
    # Recalculate total distance
    dist = sum(tsp(matrix[np.ix_([0] + slot + [0], [0] + slot + [0])])[0] for slot in slots)

# Print results
print(dist)
print(formatted_slots)

# Save results to JSON file
res = {'v0': formatted_slots}
with open('level1a_output.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)

