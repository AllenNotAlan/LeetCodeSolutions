"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #splice operator?? wut it do. need to look up
        
        nums[:] = [nums.remove(x) if x in nums for x in nums]
        print(nums)
    

    arr = [1,1,2]
    removeDuplicates(1,arr)