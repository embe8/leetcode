import re

given_string = "I123II456III78IV910"

matches = re.findall(r'([IVXLCDM]+)(\d+)', given_string)

headers = []
columns = []

for header, numbers in matches:
    headers.append(header)
    columns.append(list(numbers))

print("".join(f"{h:>5}" for h in headers))

max_rows = max(len(col) for col in columns)

for row in range(max_rows):
    print(
        "".join(
            f"{col[row] if row < len(col) else '':>5}"
            for col in columns
        )
    )

# not using re or regex

given_string = "I123II456III78IV910"
roman = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

headers, numbers = [], []
cur, is_header = "", True

for ch in given_string:
    if is_header == (ch in roman):  # still in same section
        cur += ch
    else:                           # switched section
        (headers if is_header else numbers).append(cur)
        cur, is_header = ch, not is_header

(headers if is_header else numbers).append(cur)  # flush last

numbers = [list(n) for n in numbers]
