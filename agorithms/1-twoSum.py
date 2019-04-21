#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-4-21
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# Two Sum
"""
给定一个整数数组，返回两个数字的索引，使它们相加到特定目标。
例：
 输入: nums = [2, 7, 11, 15], target = 9
 输出: return [0, 1]
"""


def twoSum1(nums, target):
    """
    来源leetcode (https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time)
    :param nums: 
    :param target: 
    :return: 
    """
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


def twoSum2(nums, target):
    """
    来源微信公众号:五分钟学算法 (https://mp.weixin.qq.com/s/3FyxT7mvxCwI3oesS3ymOg)
    :param nums: 
    :param target: 
    :return: 
    """
    left = 0
    rigth = len(nums) - 1
    while left < rigth:
        sum = nums[left] + nums[rigth]
        if sum == target:
            return left, rigth
        elif sum < target:
            left += 1
        else:
            rigth -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    targe = 9
    index1, index2 = twoSum1(nums=nums, target=targe)
    print(index1, index2)
