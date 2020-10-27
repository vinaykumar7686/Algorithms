# Longest Common Prefix

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

class Solution:
    
    def __init__(self):
        
        self.root = dict()
        
        
    def insert(self, word):
        
        curr = self.root
        
        prefix = ""
        flag = True
        
        for ch in word:
            if flag and ch in curr:
                prefix = prefix+ch
                    
            if ch not in curr:
                curr[ch] = dict()
                flag = False
                
            curr = curr[ch]
            
        return prefix                
                
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        ans = strs[0]
        first = True
        for word in strs:
            
            prefix = self.insert(word)
            
            if not first:
                print(ans[:len(prefix)], prefix)
                if ans[:len(prefix)] == prefix:
                    ans = prefix              
                
                
            first = False
            
        return ans
