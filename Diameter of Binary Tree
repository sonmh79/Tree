# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #int는 불변객체
    length = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            #자식 노드가 없다면 -1 (상태값)
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.length = max(self.length,left+right+2)
            
            #상태값 반환
            return max(left,right)+1
        dfs(root)
        return self.length
