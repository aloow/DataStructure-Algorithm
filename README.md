# DataStructure-Algorithm

## Welcome Shao qing Swift-Algorithm-Practice
- [相关概念](相关概念)
- [数据结构](数据结构)
  - [线性结构](线性结构)
  - [树](树)
- [算法](算法)
- [相关链接](相关链接)

## 相关概念
* 算法
* 数据结构
* 时间复杂度与空间复杂度 Big-O
1.how fast an algorithm is 
2.how much space it needs

## 数据结构
---------------------------------
### 线性结构  20、232、225、239(高频)
* 堆栈 Stack LIFO 
操作有：1.push、2.pop、3.peek

* 队列 Queue FIFO
操作有：1.enqueue、2.dequeue、3.peek

* 优先队列 Priority Queue 
操作有：1.enqueue、2.dequeue、3.peek

思考🤔：Stack <-> Queue 操作互相实现

* 双端队列 出栈入栈访问都可从两端进行

* 链表 单链表 双链表 
Leetcode对应的题目：
206(简单 反链表i)、92(中等 反链表ii)、24(两两交换节点)、(141、142)(有无环)、25(中等 交换节点)

### 非线性
* Set 
Leetcode对应的题目：
1、15(高频)、18

### 树 基本操作 遍历、深度、高度、路径
* 树 tree (level、root、node、leaf、children) 
<img src="https://github.com/aloow/Swift-Algorithm-Practice/blob/master/assets/BinaryTree.png" alt="" height="170" >

* 二叉树  (a tree in which each node has at most two children)
操作有：
1.插入 inserion O(h) h=tree深度、2.遍历 traversal 前序(先node,后左右) 中序(左右node) 后序(左右node) O(n)、3.search O(log n)
Leetcode对应的题目：
98(验证是否搜索二叉树)、 235、236

* 搜索二叉树 [Binary Search Trees](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Binary%20Search%20Tree)

* AVL Tree，搜索二叉树的特殊形式，满足任意节点的两个子树高最大度差为1。search O(log n)
操作：插入、删除[AVL Tree](https://www.cnblogs.com/zhuwbox/p/3636783.html)

### Hash Table 说明：通过Key存储和检索Object
collisions碰撞 1.扩大表的容量 2.链表

### Heap
* 二叉堆 插入、删除、构建二叉堆 TODO：程序员小灰中有讲解
应用：一个数组输出最大或者最小值 
最大堆：任何父节点都大于或者等于左右孩子节点
最小堆：任何父节点都小于或者等于左右孩子节点

## 算法
### 图、树相关
* DFS & BFS 
LeetCode题：102、 104、 111、22

### 动态规划
* 递归 + 存储
* 贪心算法
* 上面两者优点集成-->动态递归DP
动态递归：
* 边界
* 状态转移公式
* 最优子结构
LeetCode: 70(爬楼梯)、120(三角形最小路径和)、152()

## 代码模块
### 
### 
### 二分查找
### DP、递归递推、贪心


## 相关链接
* [维基百科](https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5)
* [raywenderlich](https://www.raywenderlich.com/990-swift-algorithm-club-swift-binary-search-tree-data-structure)
* [Swift Algorithm Club](https://github.com/raywenderlich/swift-algorithm-club)
* [力扣](https://leetcode-cn.com/)
* [leet code](https://leetcode.com/)
* [Python](https://github.com/jackfrued/Python-100-Days)
* 程序员小灰 公众号

-------------------------题外话------------------------------------------

 
 ## Python
 ### 基本数据类型
 整型(0、1)、浮点型(0.2、0.3)、字符串型('hello'、"hi")、布尔型(True、False)
 
 ### 集合类型
 数组
 ```
 list = []
 if not list:
    print('不为空')
 list.pop() # 默认最后一个元素出队
 list[-1] # 最后一个元素
 
 n = len(list)
 ```
 
 双端队列
 ```
 from collections import deque
 # 初始化
 q = deque([1])
 d = collections.deque()
 # 加元素
 q.append(1)
 # 加入另外一个数组
 q.extend([3,4,5])
 # 出队
 q.clear()
 q.popleft()
 ```
 
 
 ### 变量的使用
 ```
 
 # 全局变量,不需要声明，在类中函数里直接用
 self.res = []
 
 a = 100
 b = 12.345
 d = 'hello, world'
 e = True
 
 a, b = 5, 10
 list1.append(200)
 list1.insert(1, 400)
 list1.pop(0)
 fruits += ['pitaya', 'pear', 'mango']
 
 range(10)  # 从0开始到9 0-9
 ```
 
 ### 逻辑运算 not or and
 ```
 //逻辑与
 x and y
 //逻辑或
 a or b
 //逻辑非
 not( a and b )
 ```
 
 ### 成员运算符
 ```
 a = 10, list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):  // ( b not in list )
   print "1 - 变量 a 在给定的列表中 list 中"
else:
   print "1 - 变量 a 不在给定的列表中 list 中"
 ```

### 控制语句
if语句
```
if 3 in list1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

lst = []
if lst: # 空数组时为false，非空数组时为true
    print "不是数组"
```

for语句
```
# 遍历1到n-1的数
for i in range(1,n):
  print(i)

list1 = [1, 3, 5, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 字典的操作
for key in scores:
  print(f'{key}: {scores[key]}')
```

 while语句
 ```
 while True:
    counter += 1
 ```
 ### 函数
 ```
def lcm(x, y):
    return x * y // gcd(x, y)
 ```
 
 ### [集合](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/07.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md)
 
  ### [参考链接](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/02.%E8%AF%AD%E8%A8%80%E5%85%83%E7%B4%A0.md)
  ```
  scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
  scores['骆昊']
  if '武则天' in scores:
    print(scores['武则天'])
  for key in scores:
    print(f'{key}: {scores[key]}')
  ```
  
  ### Class 
  ```
  class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.show()


if __name__ == '__main__':
    main()
  ```
  
 -------------------------------------------------------------------

## C语言
1.NULL代表空指针

2.声明结构体
 struct ListNode {
     int val;
     struct ListNode *next;
 };
 
 2.1实例化结构体
 struct ListNode node;
 struct ListNode *pre = NULL;
 pre = &node;
 pre->next = head;

 3.声明函数 返回值在Struct后面
 struct ListNode* reverseList(struct ListNode* head){
 }
 
 4. set & get 结构体中的指针变量
 curr->perty
