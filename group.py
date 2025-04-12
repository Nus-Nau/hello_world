def create_grid():
    grid = [[0 for _ in range(7)] for _ in range(7)]
    grid[0][0] = 2
    grid[6][6] = 3
    return grid

# Test the grid
grid = create_grid()
for row in grid:
    print(row)
    
    