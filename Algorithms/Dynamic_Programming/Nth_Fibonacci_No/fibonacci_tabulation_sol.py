def fibo(n):
    '''
    Accepts integer type value as argument and returns respective number in fibonacci series.
    Uses tabulation method for computation.
    Arguments:
    n is an integer type number whose respective fibonacci nyumber is to be found.
    Returns:
    nth number in fiboacci series
    '''
    # Simply returning the value if the value of n is 0 or 1
    if n in [0,1]:
        return n
    
    # Creating an array of length n+1 and initialising it with 0.
    f = [0]*(n+1)
    # Initialising index 1 initially
    f[1] = 1

    for i in range(2, n+1):
        # calculating ith index with help of i-1 and i-2 values stored in list f
        f[i] = f[i-1]+f[i-2]
    
    return f[n]

n = int(input('Enter the number : '))
print(fibo(n))