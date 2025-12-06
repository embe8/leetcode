# Given a matrix, output it formatted in columns and rows
# Output it with headers A onwards

# Sample matrix
matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
                
rows = len(matrix)
cols = len(matrix[0])
# loop through matrix outputting each row right indented with 5 spaces
# in between elements
for row in matrix:
  formatted_row = "".join(f"{num:>5}" for num in row)
  print(formatted_row)
        
# adding headers A onwards
headers = [chr(65 + i) for i in range(cols)] # A, B, C ...
print(" " + "".join(f"{h:>5}" for h in headers))
for row in matrix:
  formatted_row = "".join(f"{num:>5}" for num in row)
  print(formatted_row)
# the "  " is for when there is a col before the numbers example:
'''  A  B  C
row1: 1 2  3
row2: 2 4  5
row3: 5 7  9
'''

# outputting each element with row and col indices
for i, row in enumerate(matrix, 1):
  for j, value in enumerate(row, 1):
    print(f"Row:{i}, Col:{j} = {value}")
    
                                                                                                                     
