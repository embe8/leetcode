'''Parse a given string and output it according to specific format (as a matrix with number of cols/rows)'''

sample_string = "123456789"

cols = 4

for i in range(0, len(sample_string), cols):
    chunk = sample_string[i:i+cols]  # means start:end ex. first iteration 0:0+4 so 1234 and then 2nd iteration 4:8 so 5678 
    print('   '.join(chunk)) # add spaces in '' to have spacesd in between each number
