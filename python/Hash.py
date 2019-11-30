# encoding: utf-8
# https://github.com/aloow/Python-100-Days/blob/master/Day01-15/07.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md 函数帮助
import os

# 242. 有效的字母异位词
# 难点：Python中对字典的用法
# 进阶点：26位数组，在s对应中加一的同时t中减一，最后遍历数组是否为零
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDic = self.getDic(s)
        tDic = self.getDic(t)
        if cmp(sDic, tDic) == 0:
            return True
        else:
            return False

    def getDic(self, s):
        dict = {'ru': '菜'}
        for i in range(len(s)):
            print(i)
            value = dict.get(str(s[i]), 0)
            value += 1
            dict[str(s[i])] = value
        return dict
        
# 1. 两数之和
# 步骤：1.第一个迭代，把nums中[值：索引]存入数组
#      2.第二个迭代，把目标值search=target-nums[i],看在表中否。

# 2. 三数之和


def main():
    solution = Solution()
    res = solution.isAnagram("aa","a")
    print(res)
 
    
if __name__ == "__main__":
    main()


