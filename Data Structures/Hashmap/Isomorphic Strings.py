$ Isomorphic Strings

'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.get_iso_code(s) == self.get_iso_code(t)
    
    def get_iso_code(self, s):
        mapping = {}
        code = ''
        count = -1
        for x in s:
            if x in mapping:
                code += mapping[x]
            else:
                count += 1
                code += str(count)
                mapping[x] = str(count)
        print(code)
        return code
    
    
    
    
    def isIsomorphic1(self, s: str, t: str) -> bool:
        hashmap = dict()
        for x,y in zip(s,t):
            if y not in hashmap.values():
                hashmap[x] = y
            
        s_trans = []
        for ch in s:
            if ch not in hashmap:
                return False
            s_trans.append(hashmap[ch])
            
        return "".join(s_trans) == t
            
            
            
