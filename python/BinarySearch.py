# encoding: utf-8
import os
from collections import deque

# 二分查找 模板代码
def binarySearch(array,tarrget):
        left, right = 0, len(array) - 1
        
        while left <= right:
            mid = (left+right)/2
            if array[mid] == tarrget:
                return tarrget
            if tarrget > array[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
# 69. x 的平方根
# 记忆点，临界点
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = (left+right)/2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                left = mid + 1
                if left*left > x:
                    return mid
            else:
                right = mid - 1
                if right*right < x:
                    return righ
    
def main():

    solut = Solution()
    res = solut.mySqrt(1)
    print(res)

#    array = [1,3,6,8,9,13,17,19,120,129,130,136,389,1999,2999,3000,3100]
#    for i in array:
#        tarrget = binarySearch(array,i)
#        print(tarrget)
    
    
 
    
if __name__ == "__main__":
    main()


