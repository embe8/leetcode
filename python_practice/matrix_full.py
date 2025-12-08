sample_string = "1 2 3 4 5 6 7 8 9"
rows = 3
cols = 3
matrix = []
# take sample string to convert to comma separated elements (list)
numbers = list(map(int, sample_string.split()))

# creating a 3x3 matrix from given sample_string
for i in range(rows):
    start = i * cols
    end = start + cols
    row = numbers[start:end]
    matrix.append(row)
    
# adding a header that's A, B, C... etc
header = [chr(65+i) for i in range(cols)]
formatted_header = "".join(f"{num:>5}" for num in header)
print(formatted_header)

for row in matrix:
    formatted_row = "".join(f"{num:>5}"for num in row)
    print(formatted_row)
