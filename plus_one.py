'''
returns int incremented by 1 where
int is represented by elements in a list
such as [1, 2, 3] representing 123
'''
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # iterate from last to first element in list
    for i in range(len(digits)-1, -1, -1):
        # if element is less than 9 add 1 then return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0 # carry over
    return [1] + digits
