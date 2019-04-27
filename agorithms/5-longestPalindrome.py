#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/26
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# Longest Palindromic Substring
"""
给出一个字符串s，从中找出最长的回文子字符串，可以假设s最长长度为1000。
例1：
 输入：babab
 输出：bab
 注意：aba也是长度为3的回文子字符串，也可以作为输出。
例2：
 输入：cbbd
 输出：bb
"""


def longestPalindrome(s):
    """
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """

    if len(s) < 2:
        return s

    longest = ''
    for i in range(len(s)):
        # 奇回文
        left_odd, right_odd = i, i
        while left_odd >= 0 and right_odd < len(s) and s[left_odd] == s[right_odd]:
            left_odd -= 1
            right_odd += 1
        odd = s[left_odd+1:right_odd]

        # 偶回文
        left_even, right_even = i, i+1
        while left_even >= 0 and right_even < len(s) and s[left_even] == s[right_even]:
            left_even -= 1
            right_even += 1
        even = s[left_even+1:right_even]

        # 比较奇偶回文跟longest的长度
        longest = max(longest, odd, even, key=len)

    return longest


if __name__ == '__main__':
    s = 'babad'
    res = longestPalindrome(s)
    print(res)
