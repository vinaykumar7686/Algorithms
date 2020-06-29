def fibo_i(n):
    '''
    Accepts integer type value as argument and returns respective number in fibonacci series.
    Uses traditional iterative technique
    Arguments:
    n is an integer type number whose respective fibonacci nyumber is to be found.
    Returns:
    nth number in fiboacci series
    '''
    # Simply returning the value if the value of n is 0 or 1
    if n in [0,1]:
        return n
    else:
        a = 0
        b = 1
        c = a+b
        while n-2>0:
            n-=1
            a=b
            b=c
            c = a+b
        return c

def fibo_r(n):
    '''
    Accepts integer type value as argument and returns respective number in fibonacci series.
    Uses traditional recursive technique
    Arguments:
    n is an integer type number whose respective fibonacci nyumber is to be found.
    Returns:
    nth number in fiboacci series
    '''
    if n in [0,1]:
        return n
    else:
        return fibo_r(n-1)+fibo_r(n-2)


n = int(input('Enter the number : '))
print(fibo_r(n))