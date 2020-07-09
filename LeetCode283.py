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