# Asteroid Collision
'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack  = []
        # if negative is largest and no one is able to break it, then that asteroid is added to this list
        villains = []
        
        while asteroids:
            
            # current asteroid
            asteroid = asteroids.pop(0)
            
            # if positive asteroid then add to stack
            if asteroid>0:
                stack.insert(0,asteroid)
                
            # if negative asteroid found
            elif asteroid<0:
                
                # converting to positive for easy further processing
                asteroid = -asteroid
                
                # flag that tell weather or not the negative asteroid is completely broken or not.
                broken = False
                
                # while the asteroids are present in stack create opponent until breaked
                while stack:
                    # define opponent for the coming negative asteroid.
                    opponent = stack[0]
                    
                    # if positive asteroid is able to stop the negative rock
                    if opponent>asteroid:
                        broken = True
                        break
                    
                    # if positive and negative asteroids are equal
                    elif opponent==asteroid:
                        stack.pop(0)
                        broken = True
                        break
                    
                    stack.pop(0)
                
                # if not negative asteroid is fully broken then add it to villains list
                if not broken:
                    villains.append(-asteroid)
        
        # append vilians and heroes left after whole process
        villains.extend(stack[::-1])
        
        return villains