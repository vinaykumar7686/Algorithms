# Implement Trie (Prefix Tree)

'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Node:
    
    def __init__(self):
        
        self.childs = [None]*26
        self.isEnd = False
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
        
    def _chr_index(self, ch):
        return ord(ch)-ord('a')
    

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        crawl = self.root
        
        n = len(word)
        
        for i in range(n):
            
            index = self._chr_index(word[i])
                        
            if crawl.childs[index] == None:
                
                crawl.childs[index] = Node()
                
            crawl = crawl.childs[index]
            
        crawl.isEnd = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        crawl = self.root
        
        n = len(word)
        
        for i in range(n):
            
            index = self._chr_index(word[i])
            
            if crawl.childs[index] == None:
                return False
            
            else:
                crawl = crawl.childs[index]
                
        if crawl.isEnd == True:
            return True
        
        else:
            return False
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        crawl = self.root
        
        n = len(prefix)
        
        for i in range(n):
            
            index = self._chr_index(prefix[i])
            
            if crawl.childs[index] == None:
                return False
            
            else:
                crawl = crawl.childs[index]
                
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
