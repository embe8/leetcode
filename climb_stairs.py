def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    one, two = 1, 1
    for i in range(n-1):
        temp = two
        two = one + two
        one = temp

    return two
