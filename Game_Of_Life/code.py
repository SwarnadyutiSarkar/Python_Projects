import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the grid
def initialize_grid(rows, cols):
    grid = np.random.choice([0, 1], size=(rows, cols), p=[0.9, 0.1])
    return grid

# Update the grid based on the Game of Life rules
def update_grid(grid):
    new_grid = grid.copy()
    rows, cols = grid.shape
    
    for i in range(rows):
        for j in range(cols):
            # Count live neighbors
            live_neighbors = np.sum(grid[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - grid[i, j]
            
            # Apply Game of Life rules
            if grid[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if live_neighbors == 3:
                    new_grid[i, j] = 1
                    
    return new_grid

# Animate the Game of Life
def animate_game_of_life(frames, grid, interval):
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='gray')
    ax.axis('off')
    
    def update(frame):
        nonlocal grid
        grid = update_grid(grid)
        img.set_array(grid)
        return img,
    
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)
    plt.show()

# Parameters
rows = 50
cols = 50
frames = 100
interval = 200

# Initialize the grid
grid = initialize_grid(rows, cols)

# Animate the Game of Life
animate_game_of_life(frames, grid, interval)
