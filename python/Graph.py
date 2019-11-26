# encoding: utf-8
import os

# 图
# BFS 广度优先 模板代码
# 树 队列 root
#def BFS(graph, start, end):
#    queue = []
#    queue.append([start])
#    visited.add(start)
#
#    while queue:
#        node = queue.pop()
#        visited.add(node)
#
#        process(node)
#        # 把所有子节点取出来，并判断是否不在visited中
#        nodes = generate_related_ends(node)
#        queue.push(nodes)

# DFS 深度优先 模板代码 102、 104、 111、22
# 树、图 队列 root
# 非递归写法
#def DFS(self, tree):
#    if tree.root is None:
#        return []
#
#    visited, stack = [], [tree.root]
#
#    while stack:
#        node = stack.pop()
#        visited.add(node)
#
#        process(node)
#        nodes = generate_related_nodes(node)
#        stack.push(nodes)
    
    
# 递归写法 模板
#visited = set()
#def dfs(node,visited):
#    visited.add(node)
#    # process current node here
#    ...
#    for next_node in node.children():
#        if not next_node in visited:
#            dfs(next_node, visited)

# 22. 括号生成 深度优先
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        left, right = n, n
        self._dfs(left, right,"")

        return self.res

    def _dfs(self, left, right, string):
        if left == 0 and right == 0:
            self.res.append(string)
            return
        # 加左括号
        if left != 0:
            string = string + "("
            left -= 1
            self._dfs(left, right, string)
        # 加右括号
        if left < right:
            string = string + ")"
            right -= 1
            self._dfs(left, right, string)
        


def main():
    solutions = Solution()
    res = solutions.generateParenthesis(1)
    print(res)
    
if __name__ == '__main__':
    main()


