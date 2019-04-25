#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/24
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# Longest Substring Without Repeating Characters
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。
例1：
 输入：“abcabcbb”
 输出：3
 说明：答案是"abc"，长度为3。
例2：
 输入：“BBBBB”
 输出：1
 说明：答案是"b"，长度为1。
例3：
 输入：“pwwkew”
 输出：3
 说明：答案是"wke"，长度为3。
"""


def lengthOfLongestSubstring(s):
    """
    时间复杂度：O（n）
    空间复杂度：O（1）
    :param s:
    :return:
    """
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:                               # 字符再字典中
            res = max(res, i - start)               # 取最长长度（当前子字符串长度与res长度对比）
            start = max(start, dic[ch] + 1)         # 更新索引位置（向前移动）
        dic[ch] = i
        print(dic)
    return max(res, len(s) - start)


if __name__ == '__main__':
    res = lengthOfLongestSubstring('abcabcbbs')
    print(res)
