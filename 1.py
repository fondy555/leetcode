"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

"""
    思路：遍历一遍nums,将nums中的值和序号以key-value形式存于字典s中,
    即例子中, s[2] = 0, 同时在遍历的过程, 计算target和n的差值，若差值在s中，直接返回序号
"""
class Solution:
    def twoSum(self, nums, target):
        s = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in s:
                return [s[m], i]
            else:
                s[n] = i