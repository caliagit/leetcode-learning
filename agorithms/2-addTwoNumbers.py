#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/22
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# Add Two Numbers
"""
给定两个非空链表，表示两个非负整数。数字以相反的顺序存储，每个节点只存储一个数字。将两个数字相加作为新链接列表返回。
假设除了数字 0 之外，每个节点的数字都不会以 0 开头。
例：
 输入：（2  - > 4  - > 3）+（5  - > 6  - > 4）
 输出： 7  - > 0  - > 8
 说明： 342 + 465 = 807
"""


def addTwoNumbers(ln1, ln2):
    """
    时间复杂度：O（n）
    空间复杂度：O（n）
    :param ln1:
    :param ln2:
    :return:
    """
    dummy = cur = ListNode(0)
    carry = 0
    while ln1 or ln2 or carry:
        if ln1:
            carry += ln1.val
            ln1 = ln1.next
        if ln2:
            carry += ln2.val
            ln2 = ln2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.next


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    ln1 = ListNode(2)
    ln1.next = ListNode(4)
    ln1.next.next = ListNode(3)

    ln2 = ListNode(5)
    ln2.next = ListNode(6)
    ln2.next.next = ListNode(4)

    res = addTwoNumbers(ln1, ln2)
    while res:
        print(res.val)
        res = res.next


