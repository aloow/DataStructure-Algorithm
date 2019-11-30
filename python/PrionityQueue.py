# encoding: utf-8
import os
from heapq import *
# 优先队列
# 实现机制
# 1. Heap(Binary, Binomial, Fibonacci)
# 2. Binary Search Tree

# leecode 703 实时判断数据流中第K大的元素
# 记忆点 最小堆 K小于arr时的处理
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        # 最大的3个元素
        self.heap = []
        if len(nums) == 0: return
        if k > len(nums):
            for i in nums:
                heappush(self.heap,i)
            return
        for i in range(0, k):
            heappush(self.heap,nums[i])
        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heapreplace(self.heap,nums[i])
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k > len(self.heap):
            heappush(self.heap,val)
            return self.heap[0]
        if val > self.heap[0]:
            heapreplace(self.heap,val)
        
        # 第K大的值
        return self.heap[0]
        
    
# leecode 239
    
def main():
    k = 3
    arr = [5,-1]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.heap)
    res = kthLargest.add(2)
    print(res)
 
 
    
if __name__ == "__main__":
    main()


