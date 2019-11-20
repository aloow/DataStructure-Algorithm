# encoding: utf-8
import os

def main():
    k = 3
    nums = [1,3,1,2,0,5]
    
#    if not nums :
#        return []
#
#    window, res = [], []
#
#    for i, x in enumerate(nums):
#        print("i = %d,x = %d" %(i,x))
#        if i >= k and window[0] <= i - k:
#            print("window.pop 0 = %d" %(window(0)))
#            window.pop(0)
#        while window and nums[window[-1]] <= x:
#            print("window.pop last")
#            window.pop()
#        print("window.append i = %d" %(i))
#        window.append(i)
#        if i >= k - 1:
#            print("res.append numsi = %d" %(nums[window[0]]))
#            res.append(nums[window[0]])
    
    if not nums :
        return []
    
    window, res = [], []
    
    for i in range(k):
        while window and nums[i] > nums[window[0]]:
            window.pop()
        window.append(i)
    
    res.append(nums[window[0]])
    
    n = len(nums)
    for i in range(k, n):
        if window and window[0] == i - k:
            window.pop(0)
        while window and nums[i] > nums[window[-1]]:
            window.pop()
        window.append(i)
        res.append(nums[window[0]])
    
    print(res)
    return res
    
    
if __name__ == '__main__':
    main()


# 二分查找
left 

# 动态规划
# 
