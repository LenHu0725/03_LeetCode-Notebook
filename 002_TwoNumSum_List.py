"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
# class ListNode:
    
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_list = []
        l1_list = ''
        l2_list = ''
        
        # 将链表读入
        while(l1 != None):
            l1_list = "{}{}".format(str(l1.val), l1_list)
            l1 = l1.next
        while(l2 != None):
            l2_list = "{}{}".format(str(l2.val), l2_list)
            l2 = l2.next
  
        # 加法运算
        sum_int = int(l1_list) + int(l2_list)
        sum_int = str(sum_int)
        
        # 链表输出 运用到数据结构知识
        sum_start = ListNode(int(sum_int[-1]))
        sum_tmp = sum_start
        
        sum_len = len(sum_int)
        for i in range(1, sum_len):
            sum_tmp.next = ListNode(int(sum_int[sum_len-i-1]))
            sum_tmp = sum_tmp.next
            
        print(type(sum_start))             
        return sum_start
             