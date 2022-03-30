"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    if x > 0 and y > 0:
        return True
    else:
        return False
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    

# Q4
def sum_digits(n):
    x = 0
    while n >= 1:
        n = int(n/10)
        x = x + n%10 + n
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"

