# encoding: utf-8
# http://c.biancheng.net/view/2432.html 函数帮助
import os
#from collections import deque

# 递归 50 169
# 模板代码
#def recursion(level,param1,param2,...):
#
#    # recursion terminator
#    if level > MAX_LEVEL:
#        print_result
#        return
#
#    # process logic in current level
#    process_data(level,data...)
#
#    # drill down
#    self.recursion(level+1,p1,...)
#
#    # reverse the current level status if needed
#    reverse_state(level)

# 菲波拉契数列 Fibonacci Queue 1、1、2、3、5、8 ...
#def fibonacci(n):
#    if n == 0: return 0
#    if n == 1: return 1
#    if n == 2: return 1
#    return fibonacci(n-1) + fibonacci(n-2)
    
# 迭代
#def fibonacci(n):
#
#    if n <= 1: return n
#
#    f0 = 0
#    f1 = 1
#    res = 0
#
#    for i in range(2,n+1):
#        res = f0 + f1
#        f0 = f1
#        f1 = res
#    return res
 
# 50. Pow(x, n) x 的 n 次幂函数 明天看视频
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0: return 0
    if n < 0:
        isNegative = True
    else:
        isNegative = False
        
    n = abs(n)
    
    f1 = x
    res = 0
    for i in range(2, n+1):
        res = x * f1
        f1 = res
    if isNegative:
        res = 1/res
    
    return res
 
def main():
    res = myPow(2,-2)
    print(res)
    
if __name__ == "__main__":
    main()


