with open('list.txt', 'r') as f:
    content = f.read()

# Parse the grid into a 2D list
lines = content.splitlines()
grid = [list(line) for line in lines]

# Dimensions of the grid
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Function to search in a specific direction
def search_direction(grid, word, start_row, start_col, delta_row, delta_col):
    length = len(word)
    end_row = start_row + delta_row * (length - 1)
    end_col = start_col + delta_col * (length - 1)
    
    # Check if the end position is within bounds
    if not (0 <= end_row < rows and 0 <= end_col < cols):
        return False
    
    # Check the word match
    for i in range(length):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        if grid[row][col] != word[i]:
            return False
    
    return True

# Search for all occurrences of the word in the grid
def find_word(grid, word):
    matches = set()  # Use a set to store unique matches
    directions = [
        (0, 1),    # Horizontal right
        (0, -1),   # Horizontal left
        (1, 0),    # Vertical down
        (-1, 0),   # Vertical up
        (1, 1),    # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),   # Diagonal down-left
        (-1, 1)    # Diagonal up-right
    ]
    
    for row in range(rows):
        for col in range(cols):
            for delta_row, delta_col in directions:
                if search_direction(grid, word, row, col, delta_row, delta_col):
                    match = ((row, col), (delta_row, delta_col))
                    matches.add(match)
    
    return len(matches)

# Find "XMAS" in all directions
total_matches = find_word(grid, "XMAS")

print("Total matches:", total_matches) # Answer was 2633

# Part Two: Find that this isn't actually an XMAS puzzle; 
# it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. 
# One way to achieve that is like this:
# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, 
# each MAS can be written forwards or backwards.
