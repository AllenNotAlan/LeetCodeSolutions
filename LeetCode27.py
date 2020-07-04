"""

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""

class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if i == val:
                nums.remove(i)
        return len(nums)


    def test(self,nums,val):

        if val not in nums:
            return len(nums)

        while val in nums:
            for i in nums:
                if i == val:
                    nums.remove(i)
        return len(nums)

    nums = [3,2,2,3]
    value = 4

    print(test(1,nums,value))
    print(nums)