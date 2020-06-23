"""
We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
    
        AList = [char for char in A]
        BList = [char for char in B]

        if AList == BList:
            return True

        if len(AList) > 0:
            count = 0
            while True:
                if count > len(AList) or AList == BList:
                    break
                else:
                    firstChar = AList[0]
                    AList.append(firstChar)
                    AList.pop(0)
                    count += 1
            
            print("%s===%s" % (AList, BList))

            if AList == BList:
                return True
            else:
                return False
        else:
            return False

    # A = "abcde"
    # B = 'cdeab'

    # A = "abcde"
    # B = "abced"

    # A = ""
    # B = "a"

    A = ""
    B = ""

    print(rotateString(1, A, B))