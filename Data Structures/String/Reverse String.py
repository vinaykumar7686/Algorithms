'''

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        
        word = ""
        ans = ""
        s = s+" "
        
        for ch in s:
            if ch!=" ":
                word = ch+word
            else:
                ans = ans+" "+word
                word = ""
                
        return ans[1:]
    
# So called inplace reversal in string :()
class Solution1:
    def reverseWords(self, s: str) -> str:
        '''
        Some security measures are ignored as the question says the string is clean
        '''
        
        def rev_word(l, h):
            
            while l<h:
                s[l], s[h] = s[h], s[l]
                l+=1
                h-=1
        
        s = list(s)
        
        i = 0
        n = len(s)
        
        l = 0
        while i<n:
            
            if s[i] == " ":
                rev_word(l,i-1)
                l = i+1
                i+=1
                
            i+=1
        
        else:
            rev_word(l, n-1)
            
        return "".join(s)                
