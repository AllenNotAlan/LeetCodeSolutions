#length of last word

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """
        :type s: str
        :rtype: int

        second solution submitted to leetcode, no filter used just list comprehension
        Runtime: 16 ms
        Memory Usage: 12.8 MB
        """
        sentence = s.split(" ")
        
        newList = [elem for elem in sentence if elem]
        word = newList[len(newList) - 1]
        res = 0
        for char in word:
            res+=1
        return(res)

    def firstSolution(self, s:str) -> int:
        """
        :type s: str
        :rtype: int

        first solution submitted to leetcode
        Runtime: 32 ms
        Memory Usage: 14 MB
        """
        sentence = s.split(" ")        
        sentence = list(filter(None, sentence))
        
        if not sentence:
            return 0
        else:
            word = sentence[len(sentence)-1]

        res = 0
        for letters in word:
            res+=1
        return res
        
    print(lengthOfLastWord(1, " a"))