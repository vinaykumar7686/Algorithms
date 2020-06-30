nums = list(map(int, (input("Enter all the numbers to be sorted (seperate with spaces ) : ")).split(" ")))
n = len(nums)
def bubble_sort(nums):
    swap = True
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            print('hey')
            if nums[j]>nums[j+1]:
                swap = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if swap==False:
            break
    return nums

print(bubble_sort(nums))