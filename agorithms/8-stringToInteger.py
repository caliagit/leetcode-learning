#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/29
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# String to Integer (atoi)
"""
实现一个将字符串转为整数的函数。
注意：
1、空格字符' '视为空字符 ，函数转换处理是应将它去除。
2、如果第一个非空字符不是整数或加减符号，则无法转换，直接返回0。
3、转换后的整数范围只能在[-2^31,2^31-1]区间,超出范围的，返回最大值INT_MAX(2^31−1)或最小值INT_MIN(−2^31)。

示例1：
 输入："42"
 输出：42
 
示例2：
 输入："  -42"
 输出：-42
 说明：减号(-)前面的空字符去掉。
 
示例3：
 输入："4193 with words"
 输出：4193
 说明："3"后面去除空字符之后不是数字，所以无法再继续转换。

示例4：
 输入："words and 987"
 输出：0
 说明：首字符不是数字，直接返回0。
 
示例5：
 输入："-91283472332"
 输出：-2147483648
 说明：-91283472332出界,返回最小值INT_MIN(-2^31-1)=-2147483648。
"""


def stringToInteger(s):
    s = s.replace(' ', '')
    if len(s) == 0:
        return 0

    res, i,  = '', 0
    if s[0] == '-':
        res = '-'
        i = 1
    while i < len(s) and s[i].isdigit():
        res += s[i]
        i += 1

    if len(res) == 0 or res == '-':
        return 0

    res = int(res)
    return max(-2**31, min(res, 2**31-1))

if __name__ == '__main__':
    s = '4193 with words'
    res = stringToInteger(s)
    print(res)
