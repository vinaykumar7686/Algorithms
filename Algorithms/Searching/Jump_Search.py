# Time Complexity : O(√n)
# Auxiliary Space : O(1)
# Limitations: Array must be sorted
import math
def accept():
    n= int (input("Enter the size of array: "))
    arr=[]
    print('Enter the Array Elements')
    while n!=0:
        n-=1
        arr.append(int(input()))

    num=int(input("Enter the number to be searched: "))

    return arr, num

def jump_search(arr, num):
    '''
    Function for Jump Search
    Parameters:
    arr is the sorted array in which number is to be searched
    num is the number to be searched
    '''
    # Storing length in n
    n = len(arr)
    # Fetching optimal step size and storing to a variable
    step_size = int(math.sqrt(n))
    # Initialising the first step's upeer pos
    step = step_size
    # Initialising first step's lower pos
    prev = 0
    
    # Searching for the value of prev and step between which the number lies
    while arr[int(min(step, n)-1)] < num:
        prev = step
        step+=step_size
        # if while increasing the step size a position comes when step's pos becomes greater than the actual size of array
        if step>n:
            return -1

    # Searching the number using linear search method between the prev and step positions
    while arr[int(prev)]<num:
        prev+=1
        if prev is min(step, n):
            return -1
    
    # Returning the index of number
    if arr[int (prev)] is num:
        return prev

    return -1

if __name__ == "__main__":
    arr, num = accept()
    
    res=jump_search(arr, num)

    if res==-1:
        print("Not Found")
    else:
        print(f'Number found at index {res}')


