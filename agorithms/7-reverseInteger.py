#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# Reverse Integer
"""
给出一个32位有符号的整数，输出它反转后的数字

示例1：
 输入：123
 输出：321

示例2：
 输入：-123
 输出：-321

示例3：
 输入：120
 输出：21

说明：因为32位有符号的整数大小范围为[-2^31,2^31-1]，所以如果反转后的整数超出了这个范围，则输出0。
"""


def reverse(x):
    r = x // max(1, abs(x))*int(str(abs(x))[::-1])
    return r if r.bit_length() < 32 or r == -2**31 else 0


if __name__ == '__main__':
    res = reverse(123)
    print(res)
