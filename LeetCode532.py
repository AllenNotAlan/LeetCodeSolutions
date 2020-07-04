from itertools import combinations
from collections import Counter

class Solution(object):

    #my solution. Passes 61 out of 72 test cases. Needs time complexity improvement
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0

        count = (Counter(combinations(nums, 2)))
        data = list({tuple(item) for item in map(sorted, count)})
        loopRange = len(data)

        noOfPairs = 0
        for i in range(loopRange):
            if data[i][0] - data[i][1] == k or data[i][1] - data[i][0] == k:
                noOfPairs += 1
        return noOfPairs

    k = 0
    exampleList = [3, 1, 4, 1, 5]
    exampleList2 = [1, 2, 3, 4, 5]
    
    exampleList4 = [1, 3, 1, 5, 4]
    
    #Submitted solution from discussion
    def test(self, nums, k):

        c = Counter(nums)
        noOfPairs = 0
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                noOfPairs += 1
        return noOfPairs

    print(test(1,exampleList4, k))
    # print(findPairs(1, exampleList3, k))