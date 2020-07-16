"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

"""
class Solution(object):
    def addOne(self, num):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num += 1
        # numToString = (str(num))
        # result = [i for i in numToString]

        # return result
        numToString = int(''.join([str(elem) for elem in num]))
        numToInt = str(((numToString) + 1))
        result = [int(i) for i in numToInt]
        # for i in numToInt:
        #     result.append(int(i))
        return result

    def discussionSolution(self, digits):

        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i]+=1
                return digits
            digits[i] = 0

        lst = []
        for i in range(n+1):
            lst.append(i)
            lst[i] = 0
        
        lst[0] = 1
        return lst
        
            


        
    #testing functions
    num = [1,2,3]

    # print(addOne(1,num)) #my submitted solution

    print(discussionSolution(1, num))
    