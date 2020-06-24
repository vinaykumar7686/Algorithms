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

def b_search_i(arr, num, l, r):
    '''
    Iterartive Function for Binary Search
    Parameters:
    arr is the sorted array in which number is to be searched
    num is the number to be searched
    l is initial index
    r in size of arry
    '''
    while l<=r:
        mid=(l+r-1)//2

        if arr[mid]==num:
            return mid
        elif arr[mid]>num:
            r=mid-1
        else:
            l=mid+1
    return -1

def b_search_r(arr, num, l, r):
    '''
    Recursive Function for Binary Search
    Parameters:
    arr is the sorted array in which number is to be searched
    num is the number to be searched
    l is initial index
    r in size of arry
    '''
    if l<=r:
        mid=(l+r-1)//2

        if arr[mid]==num:
            return mid
        elif arr[mid]>num:
            return b_search_r(arr, num, l, r=mid-1)
        else:
            return b_search_r(arr, num, l=mid+1, r=r)
    else:
        return -1

if __name__ == "__main__":
    arr, num = accept()
    
    #res=b_search_i(arr, num)
    res=b_search_r(arr, num, 0, len(arr))

    if res==-1:
        print("Not Found")
    else:
        print(f'Number found at index {res}')


