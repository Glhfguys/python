from PIL import Image
import numpy as np
import heapq
import random

# Function to split the image into 3x3 parts
def split_image(image):
    height, width = image.size
    split_images = []
    h, w = height // 3, width // 3
    for i in range(3):
        for j in range(3):
            box = (j * w, i * h, (j + 1) * w, (i + 1) * h)
            split_images.append(image.crop(box))
    return split_images

# Function to shuffle the images randomly
def shuffle_images(images):
    random.shuffle(images)
    return images

# Function to display the images
def display_images(images):
    for img in images:
        img.show()

# Function to calculate the misplaced tiles heuristic
def misplaced_tiles(current_state, goal_state):
    misplaced = 0
    for i in range(9):
        if current_state[i] != goal_state[i]:
            misplaced += 1
    return misplaced

# Function to perform A* search
def astar_search(start_state, goal_state):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(0, start_state, '')]
    heapq.heapify(queue)
    visited = set()
    
    while queue:
        cost, current_state, path = heapq.heappop(queue)
        if current_state == goal_state:
            return path
        visited.add(current_state)
        zero_index = current_state.index('0')
        x, y = zero_index // 3, zero_index % 3
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_index = nx * 3 + ny
                next_state = list(current_state)
                next_state[zero_index], next_state[next_index] = next_state[next_index], next_state[zero_index]
                next_state_str = ''.join(next_state)
                if next_state_str not in visited:
                    heapq.heappush(queue, (misplaced_tiles(next_state, goal_state), next_state_str, path + str(next_index)))

# Load the image
image = Image.open('image.jpg')

# Split the image into 3x3 parts
split_images = split_image(image)

# Shuffle the images randomly
shuffled_images = shuffle_images(split_images)

# Display the shuffled images
display_images(shuffled_images)

# Construct the initial state string
start_state = ''.join([str(i) for img in shuffled_images for i in np.array(img).flatten()])

# Define the goal state (sorted order of tiles)
goal_state = '123456780'

# Perform A* search to solve the puzzle
solution = astar_search(start_state, goal_state)

print("Solution:", solution)
