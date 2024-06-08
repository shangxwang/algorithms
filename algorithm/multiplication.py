def karatsuba(num1, num2):
    """
    Karatsuba algorithm for multiplication.
    :param array: two numbers (num1, num2)
    :return: result of num1*num2
    """
    if num1 < 10 and num2 < 10:
        return num1 * num2
    n = max(len(str(num1)), len(str(num2)))
    m = n//2  
    x_h = num1//(10**m)
    x_l = num1%(10**m)
    y_h = num2//(10**m)
    y_l = num2%(10**m)

    a = karatsuba(x_h, y_h)
    d = karatsuba(x_l, y_l)
    e = karatsuba(x_h + x_l , y_h + y_l) - a - d
    return a*(10**(m*2)) + e*(10**m) + d