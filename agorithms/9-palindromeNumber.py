#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-4-30
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# Palindrome Number
"""
给出一个整数，判断它是否为回文整数。如果是，输出true，否则输出false。

示例1：
 输入：121
 输出：true

示例2：
 输入：-121
 输出：false
 说明：从左到右为-121，从右到左为121-，因此它不是回文。

示例3：
 输入：10
 输出：false
 说明：从右到左为01，因此它不是回文。
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    l2r, r2l = x, 0
    while l2r > 0:
        r2l *= 10
        r2l += int(l2r % 10)
        l2r = int(l2r / 10)
    return r2l == x


def isPalindrome2(x):
    """
    :type x: int
    :rtype: bool
    """
    return x >= 0 and x == int(str(x)[::-1])

if __name__ == '__main__':
    x = 121
    res = isPalindrome(x)
    print(res)
