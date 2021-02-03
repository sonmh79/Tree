# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #재귀 구조로 높이 판별
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            
            if left == -1 or right == -1 or \
            abs(left-right) >1:
                return -1
            # 밑에서부터 높이(상태값) 1씩 증가
            return max(left,right)+1
        return check(root) != -1
