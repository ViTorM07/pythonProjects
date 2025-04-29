def gdc(a , b):
    assert a > 0 and b>0
    while a != 0:
        if a > b:
            a -= b
        else:
            b -=a
    return a

def gcd(a, b):
    assert a > 0 and b > 0
    if a == b:
        return a
    elif a>b:
        return gcd(b, a-b)
    else:
        return gcd(a, b-a)