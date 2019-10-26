# Swift-Algorithm-Practice
Algorithms && Data structures

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

## 算法

## 相关链接
* [维基百科](https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5)
* [raywenderlich](https://www.raywenderlich.com/990-swift-algorithm-club-swift-binary-search-tree-data-structure)
* [Swift Algorithm Club](https://github.com/raywenderlich/swift-algorithm-club)
* [力扣](https://leetcode-cn.com/)
* [leet code](https://leetcode.com/)
* [Python](https://github.com/jackfrued/Python-100-Days)
* 程序员小灰 公众号

-------------------------题外话------------------------------------------
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
 
 ## Python
 class、func、for in 、变量、dictionary、array是否为空 
 实例化一个类
  while、if、for
  函数声明
  逻辑运算
  
 -------------------------------------------------------------------

