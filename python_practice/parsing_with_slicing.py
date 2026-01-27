'''Parse a given string and output it according to specific format (as a matrix with number of cols/rows)'''

sample_string = "123456789"

cols = 4

for i in range(0, len(sample_string), cols):
    chunk = sample_string[i:i+cols]
    print(''.join(chunk))
