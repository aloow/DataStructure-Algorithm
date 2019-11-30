# encoding: utf-8
# http://c.biancheng.net/view/2432.html 函数帮助
import os

# Tree
# 搜索二叉树：
# 1.节点的左子树只包含小于节点的数
# 2.节点的右子树只包含大于节点的数
# 3.所有左子树和有子树子树也必须是搜索二叉树

# leetcode 98、235、236

# 98 验证二叉搜索树
#class Solution(object):\
#    def isValidBST(self, root):
#        """
#        :type root: TreeNode
#        :rtype: bool
#        """
#        def helper(node, lower = float('-inf'), upper = float('inf')):
#            if not node:
#                return True
#
#            val = node.val
#            if val <= lower or val >= upper:
#                return False
#
#            if not helper(node.right, val, upper):
#                return False
#            if not helper(node.left, lower, val):
#                return False
#            return True
#        return helper(root)

# 94. 二叉树的中序遍历 先左子树，然后根部，最后右子树
#class Solution(object):
#    def isValidBST(self, root):
#        """
#        :type root: TreeNode
#        :rtype: bool
#        """
#        res = self.inorderTraversal(root)
#        for i in range(len(res)-1):
#            if res[i] >= res[i+1]:
#                return False
#        return True
#
#    def inorderTraversal(self, root):
#        """
#        :type root: TreeNode
#        :rtype: List[int]
#        """
#        res = []
#        def view(node):
#            if not node: return
#            view(node.left)
#            res.append(node.val)
#            view(node.right)
#
#        view(root)
#        return res
            
# 235. 二叉搜索树的最近公共祖先
# 分叉时，要记得返回
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#
#class Solution(object):
#    def lowestCommonAncestor(self, root, p, q):
#        """
#        :type root: TreeNode
#        :type p: TreeNode
#        :type q: TreeNode
#        :rtype: TreeNode
#        """
#
#        parent_val = root.val
#        p_val = p.val
#        q_val = q.val
#
#        if p_val < parent_val and q_val < parent_val:
#            return self.lowestCommonAncestor(root.left, p, q)
#        elif p_val > parent_val and q_val > parent_val:
#            return self.lowestCommonAncestor(root.right, p, q)
#        else:
#            return root
    
#236. 二叉树的最近公共祖先
  
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        
        # 遍历左子树，是否包含p q,在的话，把左子树设为root，继续遍历
        if root.left:
        parr = view()
        view(root.left,parr)
        for
        # 遍历右子树，是否包含p q,在的话，把右子树设为root，继续遍历
        
        # 把这个节点返回 为结果
    
    
    def view(self, node, array):
        if not node: return
        
        view(node.left,array)
        array.append(node.val)
        view(node.right,array)
    
def main():
    lnode = TreeNode(2)
    rnode = TreeNode(8)
    root = TreeNode(6)
    root.left = lnode
    root.right = rnode
    
    llnode = TreeNode(0)
    lrnode = TreeNode(4)
    lnode.left = llnode
    lnode.right = lrnode
    
    lrlnode = TreeNode(3)
    lrrnode = TreeNode(5)
    lrnode.left = lrlnode
    lrnode.right = lrrnode
    
    rlnode = TreeNode(7)
    rrnode = TreeNode(9)
    rnode.left = rlnode
    rnode.right = rrnode
    
    solution = Solution()
    res = solution.lowestCommonAncestor(root,lrlnode,llnode)
    print(res)

 
 
    
if __name__ == "__main__":
    main()

# 正负无穷
# float("inf"), float("-inf")
