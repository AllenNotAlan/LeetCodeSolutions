"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]


"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 

        for i in nums:
            # print(nums[i])
            if i == 0:
                nums.append(i)
                nums.remove(i)

        return nums

    nums = [0,1,0,3,12]
    test1 = [0,0,1]
    print(moveZeroes(1,test1))
    # moveZeroes(1,test1)