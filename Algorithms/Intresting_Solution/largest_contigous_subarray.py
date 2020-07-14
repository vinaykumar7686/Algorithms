'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
def maxSubArray(nums):
        '''
        Kadane's Algorithm 
        Time Complexity = O(1)
        '''
        '''maxsum = max(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sub_sum = sum(nums[i:j+1])
                if sub_sum>maxsum:
                    maxsum = sub_sum
        return maxsum'''
        if min(nums)>=0:
            return sum(nums)
        elif max(nums)<=0:
            return max(nums)
        
        meh = 0
        msf = min(nums)
        for num in nums:
            meh = meh+num
            
            if meh<num:
                meh = num
            
            if meh>msf:
                msf = meh
                
        return msf

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))