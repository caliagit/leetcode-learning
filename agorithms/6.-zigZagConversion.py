#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/27
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# ZigZag Conversion
"""
将字符串“PAYPALISHIRING”按照给定的行数（numRows）进行zigZag排序，输出排序后的结果。

Z排序示例(numRows=3)：
P   A   H   N
A P L S I I G
Y   I   R

Z排序示例(numRows=4)：
P     I    N
A   L S  I G
Y A   H R
P     I

例1：
 输入：s = "PAYPALISHIRING", numRows = 3
 输出：return "PAHNAPLSIIGYIR"

例2：
 输入：s = "PAYPALISHIRING", numRows = 4
 输出：return "PINALSIGYAHRPI"
"""


def zigZagConversion(s, numRows):
    """
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    if numRows ==1 or numRows >= len(s):
        return s

    cl = [''] * numRows
    index, step = 0, 1
    for x in s:
        cl[index] += x              # 将index相同的字符按先后顺序连接起来
        if index == 0:              # index在首行，需要往下移动，step=1
            step = 1
        if index == numRows - 1:    # index在尾行，需要往上移动，step=-1
            step = -1
        index += step
    return ''.join(cl)


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 3
    res = zigZagConversion(s=s, numRows=numRows)
    print(res)
