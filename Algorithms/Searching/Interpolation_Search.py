# Time Complexity: O(log(n))
def accept():
    n= int (input("Enter the size of array: "))
    arr=[]
    print('Enter the Array Elements')
    while n!=0:
        n-=1
        arr.append(int(input()))

    num=int(input("Enter the number to be searched: "))

    return arr, num

def interpolation_search_i(arr, x, n):
    '''
    Iterartive Function for Interpolation Search
    Parameters:
    arr is the sorted array in which number is to be searched
    x is the number to be searched
    n is size or array
    '''
    # Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1; 
      
    return -1
            

def interpolation_search_r(arr, num, l, r):
    '''
    Recursive Function for Intepolation Search
    Parameters:
    arr is the sorted array in which number is to be searched
    num is the number to be searched
    l is initial index
    r in size of arry
    '''
    if l<=r and arr[l]<=num and arr[r]>=num:
        if l is r:
            if arr[l] is num:
                return l
            else:
                return -1

        pos  = l + int(((float(r - l) / ( arr[r] - arr[l])) * ( num - arr[l]))) 

        if arr[pos]==num:
            return pos
        
        elif arr[pos]>num:
            interpolation_search_r(arr, num, pos+1, r)
        else:
            interpolation_search_r(arr, num, l, pos-1)
    
    return -1
            


if __name__ == "__main__":
    arr, num = accept()
    
    #res=interpolation_search_i(arr, num, len(arr))
    
    res=interpolation_search_r(arr, num, 0, len(arr)-1)
    if res==-1:
        print("Not Found")
    else:
        print(f'Number found at index {res}')


