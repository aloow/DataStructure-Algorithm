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

### 线性结构 
* 堆栈 Stack LIFO 
操作有：1.push、2.pop、3.peek

* 队列 Queue FIFO
操作有：1.enqueue、2.dequeue、3.peek

思考🤔：Stack <-> Queue 操作互相实现

* 链表 单链表 双链表 
Leetcode对应的题目：
206(简单 反链表i)、92(中等 反链表ii)、24(两两交换节点)、(141、142)(有无环)、25(中等 交换节点)


### 树
* 树 tree (level、root、node、leaf、children) 
<img src="https://github.com/aloow/Swift-Algorithm-Practice/blob/master/assets/BinaryTree.png" alt="" height="170" >

* 二叉树  (a tree in which each node has at most two children)
操作有：
1.插入 inserion O(h) h=tree深度、2.遍历 traversal 前序(先node,后左右) 中序(左右node) 后序(左右node) O(n)、3.search O(log n)

* 搜索二叉树 [Binary Search Trees](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Binary%20Search%20Tree)

## 算法

## 相关链接
* [维基百科](https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5)
* [raywenderlich](https://www.raywenderlich.com/990-swift-algorithm-club-swift-binary-search-tree-data-structure)
* [Swift Algorithm Club](https://github.com/raywenderlich/swift-algorithm-club)
* [力扣](https://leetcode-cn.com/)
* [leet code](https://leetcode.com/)
* [Python](https://github.com/jackfrued/Python-100-Days)

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
 
 
 -------------------------------------------------------------------

