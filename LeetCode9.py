#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numToString = str(x)
        stringAsList = list(numToString)
        stringAsList.reverse()
        numStr = ''.join(stringAsList)
        
        if numToString == numStr:
            return True
        else:
            return False

    print(isPalindrome(1,-121))