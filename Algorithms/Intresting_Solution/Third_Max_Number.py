class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        v = [float('-inf')] * 3
        for num in nums:
            if num in v:
                continue
            if num > v[0]:   v = [num, v[0], v[1]]
            elif num > v[1]: v = [v[0], num, v[1]]
            elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]