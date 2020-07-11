# Question Source: Leetcode (https://leetcode.com/articles/single-number/)
'''
136. Single Number 

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
Solution

'''
def my_approach(nums):
    for i in range(len(nums)):
        if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
            return nums[i]

def bit_manipulation(nums):
    '''
    Concept

    If we take XOR of zero and some bit, it will return that bit
    a \oplus 0 = aa⊕0=a
    If we take XOR of two same bits, it will return 0
    a \oplus a = 0a⊕a=0
    a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
    So we can XOR all bits together to find the unique number.

    Complexity Analysis

    Time complexity : O(n)O(n). We only iterate through \text{nums}nums, so the time complexity is the number of elements in \text{nums}nums.

    Space complexity : O(1)O(1).
    '''
    a = 0
    for i in nums:
        a ^= i
    return a

def math_approach(nums):
    return 2 * sum(set(nums)) - sum(nums)

def hash_table_approach(nums):
    from collections import defaultdict
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
    
    for i in hash_table:
        if hash_table[i] == 1:
            return i


