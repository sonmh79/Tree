# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #후위 순회
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left,t2.left)
            node.right = self.mergeTrees(t1.right,t2.right)
            return node
        # 둘 중 하나만 있다면 있는 값 리턴
        else:
            return t1 or t2
        
