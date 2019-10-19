# Swift-Algorithm-Practice
Algorithms && Data structures

## Welcome Shao qing Swift-Algorithm-Practice
- [相关概念](相关概念)
- [数据结构](数据结构)
  - [线性结构](线性结构)
  - [树](树)
  
  
## 相关概念
* 算法
* 数据结构
* 时间复杂度与空间复杂度 Big-O
1.how fast an algorithm is 
2.how much space it needs

## 数据结构

### 线性结构
* 堆栈 Stack LIFO 
操作有：push、pop、peek
* 队列 Queue FIFO
操作有：enqueue、dequeue、peek

### 树
* 一般的树 tree 
<img src="https://github.com/aloow/Swift-Algorithm-Practice/blob/master/assets/BinaryTree.png" alt="" height="170" >
* 二叉树
* 搜索二叉树 Binary Search Trees(BST)

## 算法

## Sore （Goal: Sort an array from low to high (or high to low).）
### Insertion Sort 插入排序，平时打牌的时候就是这种
### In-place sort 就地排序，冒泡排序

## Binary Search （Goal: Quickly find an element in an array.）
### Linear Search 线性搜索 一个个对比
### Divide and conquer 二分法 log2(1000000) = 19.9
### Iterative vs recursive ?? 待续





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

