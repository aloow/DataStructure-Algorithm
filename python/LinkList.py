# encoding: utf-8
import os

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#链表

# 反转一个单链表： 完成
# 输入: head->1->2->3->NULL 输出: head->3->2->1->NULL
# 记录点：pre、cur(head)、tmp
# 难点：无
# 遗留点：还可用递归
def reverseList(head):
    pre = None
    cur = head
    tmp = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

# 237. 删除链表中的节点
# 记录点：val <- next.val, 再删除
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next

# 19. 删除链表的倒数第N个节点
# TODO:
def removeNthFromEnd(head, n):
    if not head:
        return head
    tmp = head
    a, b = tmp ,tmp.next
    while n > 0 and b:
        n = n-1
        b = b.next
    
    if n != 0 or not b:
        return head
    
    while b.next
        a, b = a.next, b.next
    a.next = a.next.next
    
    return head
#    # 增加一个特殊节点方便边界判断
#    p = ListNode(-1)
#    p.next,a,b = head,p,p
#    # 第一个循环，b指针先往前走n步
#    while n>0 and b:
#        b,n = b.next,n-1
#    # 假设整个链表长5，n是10，那么第一次遍历完后b就等用于空了
#    # 于是后面的判断就不用做了，直接返回
#    if not b:
#        return head
#    # 第二次，b指针走到链表最后，a指针也跟着走
#    # 当遍历结束时，a指针就指向要删除的节点的前一个位置
#    while b.next:
#        a,b = a.next,b.next
#    # 删除节点并返回
#    a.next = a.next.next
#    return p.next
    
    # 141. 环形链表 完成
    # 注意点：1. if not (head and head.next)  2. a, b = h, h.next
    def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if not (head and head.next):
                return False
            #定义两个指针i和j，i为慢指针，j为快指针
            i,j = head,head.next
            while j and j.next:
                if i==j:
                    return True
                # i每次走一步，j每次走两步
                i,j = i.next, j.next.next
            return False

    
def main():
    #


if __name__ == "__main__":
    main()


