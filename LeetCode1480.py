"""
Running Sum of 1D Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i])

Return the running sum of nums.

"""
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None

        runningList = []

        total = 0
        for i in nums:
            total += i
            runningList.append(total)
        
        return runningList

    test1 = [1,2,3,4]
    test2 = [1,1,1,1,1]
    test3 = []
    test4 = [3,1,2,10,1]


    # print(testSolution(1,test1))
    # print(testSolution(1,test2))
    # print(testSolution(1,test3))
    # print(testSolution(1,test4))