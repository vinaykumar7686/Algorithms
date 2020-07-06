# Time Complexity = O(N^2)
nums = list(map(int, (input("Enter all the numbers to be sorted (seperate with spaces ) : ")).split(" ")))
n = len(nums)
def selection_sort(nums, n):
    i=0
    while i<n-1:
        # Initialising minimum index (index that is to be worked upon)
        mi = i

        j = i+1

        while j<n:
            # Seraching for index of least value in unsorted sub-array
            if nums[j]<nums[mi]:
                mi = j
            
            j+=1
        
        #Swaping the value at mi index with the least value in unsorted sub array
        nums[mi], nums[i] = nums[i], nums[mi]

        i+=1
    return nums

print(selection_sort(nums, n))