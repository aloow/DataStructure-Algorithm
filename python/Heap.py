# encoding: utf-8
# http://c.biancheng.net/view/2432.html 函数帮助
import os
# 堆


class heap(object):
    # 创建
    def __init__(self, list):
        self.array = list

    # 上浮
    def upAdjust(self,list)
    
    
    
    # 下沉
    def downAdjust(self,list)
    
    
    
    
def main():
 
 
 
 
    
if __name__ == "__main__":
    main()

""" 堆 根叫堆顶
目录：
1.什么是二叉堆 是一种数据结构
1.1二叉堆的插入、
1.2删除
1.3构建
2.堆排序算法
3.优先队列
3.1普通队列FIFO
3.2优先队列之最大优先队列
3.2优先队列之最小优先队列
3.3大顶堆实现最大优先队列
3.4小顶堆实现最小优先队列
4.快速排序、归并排序、堆排序时间复杂度空间复杂度比较

数据结构： 二叉堆 本质上是一种完全二叉树，它分为两个类型：
1.最大堆:任何一个父节点的值，都大于等于它左右孩子节点的值
2.最小堆:任何一个父节点的值，都小于等于它左右孩子节点的值

一、二叉堆
插入节点：O(lng n)
插入堆中最后一个位置
上浮
删除节点：O(lng n)
删除所在节点
下沉
构建二叉堆：O(n lng n)
依次对非叶子节点进行下沉操作


二、堆排序算法 O(n lng n)
步骤：
1.把无序数组构建成二叉堆
2.循环删除堆顶元素，堆进行自我调整

三、优先队列 是一种算法，
普通队列：
先进先出 FIFO
最大优先队列：
无论入队顺序，都是最大出
最小优先队列：
无论入队顺序，都是最小出
数据结构实现它：
TODO二叉堆的实现


四、几个排序时间复杂度空间复杂度比较
                快速排序      堆排序       归并排序
最坏情况            n^2      O(n logn)   O(n logn)
平均时间复杂度    O(n logn)   O(n logn)  O(n logn)
空间复杂度           O(n)       O(1)        O(n)


其他：
node
lsubNode = 2*node + 1
rsubNode = 2*node + 2
"""


