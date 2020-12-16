# Merge Sorted Array

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n

HINTS
You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n2 = len(nums2)-1
        n = len(nums1)-1
        n1 = n - n2 - 1
        
        while n2>-1 and n1>-1:
            
            if nums1[n1]<nums2[n2]:
                nums1[n] = nums2[n2]
                n2-=1
                n-=1
            else:
                nums1[n] = nums1[n1]
                n1-=1
                n-=1
                
        if n1<=-1:
            for i in range(n2+1):
                nums1[i] = nums2[i]
