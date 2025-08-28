def addBinary(a, b):
    # Make both strings the same length by padding with zeros on the left
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)

    result = ""
    carry = 0

    # Loop from right to left
    for i in range(max_length - 1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])

        total = bit_a + bit_b + carry
        bit_result = total % 2      # What goes in the current position
        carry = total // 2          # What gets carried to the next left bit

        result = str(bit_result) + result  # Prepend the bit to the result

    # If there's a leftover carry, add it at the beginning
    if carry:
        result = "1" + result

    return result
