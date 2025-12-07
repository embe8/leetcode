sample_string = "1 2 3 4 5 6 7 8 9"
rows = 3
cols = 3
matrix = []
# reading string input and creating a matrix from it

# input().split() to split string into comma separated elements e.g. 1234 to 1, 2, 3, 4
# use map to convert it to int map(int, input().split())) and then convert to list
# then append to matrix (each list is a row)
for i in range(rows):
  row = list(map(str, sample_string.split()))
  start = i * cols          # Starting index for this row
  end = start + cols        # Ending index for this row
  row = row[start:end]  # Slice the list
  matrix.append(row)
  
for row in matrix:
    formatted_row = "".join(f"{num:>5}"for num in row)
    print(formatted_row)
