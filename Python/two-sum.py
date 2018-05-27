# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return [k - 1, tmp_nums.index(j) + k]
           
    def twoSum3(self, nums, target):  # mine
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = len(nums)
        for i in range(0, k, 1):
            for j in range(i+1, k, 1):
                if  (nums[i] + nums[j]) == target:
                    return [i, j]



if __name__ == '__main__':
    print Solution().twoSum((2, 7, 11, 15), 9)
