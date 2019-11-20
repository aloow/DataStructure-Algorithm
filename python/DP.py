# encoding: utf-8
import os

# 动态规划
# 题目一：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
class Test:

    def climbStairs(self, n):
        if n<3 :
            return n
        else:
            a = climbStairs(n-1)
            b = climbStairs(n-2)
            return  a + b

#题目2：
#给定一个整数数组nums，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）
def maxSubArray(nums):
    cur_sum=0
    res=nums[0]
    n = len(nums)
    for i in range(n): #0开始 不到n
        if cur_sum>0:
            cur_sum+=nums[i]
        else:
            cur_sum=nums[i]
        res = max(res,cur_sum)
    return res

#def maxSubArray(self, nums: List[int]) -> int:
#    cur_sum=0
#    res=nums[0]
#    n=len(nums)
#    for i in range(n):
#        if(cur_sum>0):
#            cur_sum+=nums[i]
#        else:
#            cur_sum=nums[i]
#        res=max(res,cur_sum)
#    return res
    
def main():
    maxSubArray([1])

if __name__ == "__main__":
    main()


