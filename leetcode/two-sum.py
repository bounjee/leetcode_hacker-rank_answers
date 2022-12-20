class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sets = {}
        for i, num in enumerate(nums):
            if target - num in sets:
                return [sets[target-num], i]
            sets[num] = i
        return []

# s1 = Solution
# print(s1.twoSum(nums=[2,7,5,4],target=9))