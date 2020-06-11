"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

ie:

J = 'aA', S = 'aAAbbbb'
Output: 3
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        jewels = [ord(char) for char in J]
        stones = [ord(char) for char in S]
        
        noOfJewels = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    noOfJewels = noOfJewels + 1
        
        return noOfJewels
        

    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(1,J,S))