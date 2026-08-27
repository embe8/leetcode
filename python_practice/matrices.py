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

sample_string = "123456789"
# reading string input and creating a matrix from it

# input().split() to split string into comma separated elements e.g. 1234 to 1, 2, 3, 4
# use map to convert it to int map(int, input().split())) and then convert to list
# then append to matrix (each list is a row)
for i in range(rows):
  row = list(map(int, sample_string.split()))
  matrix.append(row)

# with number of columns and rows known, creating a 2d array/matrix and printing as a table
digits = "123456"

rows = 3
cols = 2

matrix = []
# create matrix
matrix = []
for i in range(rows):          # i = 0, 1
    start = i * cols
    end = (i + 1) * cols
    matrix.append(digits[start:end])
# print in table format
for row in matrix:
    print("".join(f"{num:>5}"for num in row))
# CASE
# if needed to split into rows when an element is encountered
# sample is # in this case
sample = "12#345#6"

matrix = [[int(d) for d in chunk] for chunk in sample.split("#")]
print(matrix)  # [[1, 2], [3, 4, 5], [6]]

# CASE with PADDING
digits = "1#23##45#6"
#output has empty cells if we do not pad
#[[1], [2, 3], [0], [4, 5], [6]]
#    1
#    2    3
#    0
#    4    5
#    6
# get max col length
matrix = [[int(d) for d in chunk] if chunk else [0] for chunk in digits.split('#')]
max_col = max(len(row) for row in matrix)
matrix = [row + [0] * (max_col - len(row)) for row in matrix]
for row in matrix:
    print("".join(f"{digit: >5}" for digit in row))
