#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/25
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# Median of Two Sorted Arrays
"""
有两个长度分别为m和n的已排序数组nums1、nums2，输出这两个数组的中位数，要求运行时间复杂度为O（log(m+n)）
例1：
 输入：nums1 = [1,3], nums2 = [2]
 输出：2
例2：
 输入：nums1 = [1,2]，nums2 = [3,4]
 输出：（2 + 3）/ 2 = 2.5
"""


def findMedianSortedArrays(A, B):
    """
    时间复杂度：O（log(m+n)）
    空间复杂度：O（1）
    """
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m

    imin, imax, half_len = 0, m, int((m + n + 1) / 2)
    while imin <= imax:
        i = int((imin + imax) / 2)
        j = half_len - i
        if i < m and B[j - 1] > A[i]:
            imin = i + 1     # i 太小，需要增加
        elif i > 0 and A[i - 1] > B[j]:
            imax = i - 1    # i 太大，需要减小
        else:
            # i 处于最佳位置
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    A = [1, 2]
    B = [3, 4]
    res = findMedianSortedArrays(A, B)
    print(res)
