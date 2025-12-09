# Pattern 1: Read dimensions and matrix
rows, cols = map(int, input().split())
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Pattern 2: Iterate through matrix
for row in matrix:
    for num in row:
        # do something

# Pattern 3: Access by indices
for i in range(rows):
    for j in range(cols):
        value = matrix[i][j]

# Pattern 4: Column iteration
for col in range(cols):
    for row in range(rows):
        value = matrix[row][col]

# Pattern 5: Format output with width
print(f"{value:>5}")  # right-align, width 5
print(f"{value:<5}")  # left-align, width 5

# Pattern 6: Join with spaces
print(" ".join(map(str, row)))
