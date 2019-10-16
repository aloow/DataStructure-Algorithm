# Swift-Algorithm-Practice
算法与数据结构

Algorithms && Data structures

The goal of this project is to explain how algorithms work

Big-O :
1.how fast an algorithm is 
2.how much space it needs


## Begin 
-------------------------------------------------------------------
### Stacks LIFO
push to add a new element to the top of the stack
pop to remove the element from the top
peek at the top element without popping it off

### Queue FIFO
enqueue 
dequeue

## Sore （Goal: Sort an array from low to high (or high to low).）
### Insertion Sort 插入排序，平时打牌的时候就是这种
### In-place sort 就地排序，冒泡排序

## Binary Search （Goal: Quickly find an element in an array.）
### Linear Search 线性搜索 一个个对比
### Divide and conquer 二分法 log2(1000000) = 19.9
### Iterative vs recursive ?? 待续


-------------------------------------------------------------------

## Star
### 数组与链表


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
 
 
 -------------------------------------------------------------------
 ## 做算法题的经验
 先把步骤一步步纸上预演一遍
 再编程
