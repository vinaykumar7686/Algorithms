'''
Subarray Sum Equals K
Medium

4970

167

Add to List

Share
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashset = collections.defaultdict(int)
        s = 0
        count = 0
        hashset[0] = 1
        for num in nums:
            s = s + num
            if s-k in hashset:
                count+=hashset[s-k]
            hashset[s] +=1
        return count