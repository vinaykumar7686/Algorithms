def fibo( n , lookup ):
    '''
    fibo is a recursive function that returns the fibonacci number at nth index.
    Arguments:
    n is an integer type number whose respective fibonacci nyumber is to be found.
    lookup is an list in which the calculated values are stored for future use.
    Returns:
    Nth number in fibonacci series.
    '''
    # base condiations
    if n is 1 or n is 0:
        lookup[n] = n
    else:
        # Assiging lookup for nth index with sum of values at index n-1 and n-2 in lookup list.
        lookup[n] = fibo(n-1, lookup)+fibo(n-2, lookup)
    return lookup[n]


n = int(input("Enter the number : "))

# Creatig and initialising a lookup list in which calculated values are stored for future use.
lookup = [None]*(n+1)

print(fibo(n ,lookup))


