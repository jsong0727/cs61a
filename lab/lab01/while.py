def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    flag = 0
    while n > 0:
        n, d = n // 10, n % 10
        if d == 8 and flag == 1:
            return True
        elif d == 8:
            flag = 1
        else:
            flag = 0
    return False

double_eights(889765)