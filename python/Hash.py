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
    # 无重复字符的最长子串
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in range(len(s)):
            value = dict.get(str(s[i]), 0)
            value += 1
            dict[str(s[i])] = value
        
        defV = dict.get("name",10)
        name = dict.get("name")
        print(defV)
        print(name)
# 1. 两数之和
# 步骤：1.第一个迭代，把nums中[值：索引]存入数组
#      2.第二个迭代，把目标值search=target-nums[i],看在表中否。

# 2. 三数之和


def main():
    solution = Solution()
    solution.lengthOfLongestSubstring("pwwkew")

 
    
if __name__ == "__main__":
    main()

'''
字典的使用:
初始化:
dict = {}
字典长度：
length = len(dict)
取值,如果键不存在，返回默认值。不会设置默认值到key中
dict.get(key, default=None)  使用：dict('name') dict('name', 10)
是否存在
dict.has_key(key)
返回所有
dict.keys() dict.values()
设置值
dict[key] = valut
清空
dict.clear()

字符变字符串  '2' ->  str('2')
'''
