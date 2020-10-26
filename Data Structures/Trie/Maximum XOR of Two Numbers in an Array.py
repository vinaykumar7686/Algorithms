# Maximum XOR of Two Numbers in an Array

'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1
'''

class Solution:
    def __init__(self):
        self.root = {}

    def insert(self, num):

        curr = self.root

        i = 0
        while i<32:

            if num[i] not in curr:
                curr[num[i]] = dict()

            curr = curr[num[i]]
            i+=1

    def get_max_xor(self,num):

        i = 0

        curr = self.root
        val = ""
        while i<32:

            req = str(1-int(num[i]))

            if req in curr:
                val = val+req
                curr = curr[req]

            else:
                val = val+num[i]
                curr = curr[num[i]]

            i+=1

        return int(num,2) ^ int(val, 2)
    
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        for num in nums:
            self.insert(bin(num)[2:].zfill(32))
            
        # print(self.root)
        
        ans = 0
        for num in nums:
            ans = max(ans, (self.get_max_xor(bin(num)[2:].zfill(32))))
        
        
        return ans
