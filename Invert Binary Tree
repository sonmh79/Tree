# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # My Solution!!
    # Sucess !
    # Runtime 44ms / Memory Usage: 14.3MB
    # BFS
    def invertTree(self, root: TreeNode) -> TreeNode:
        r = root
        def bfs(node):
            #끝까지 가면 종료
            if not node:
                return
            #좌,우 바꾸기
            node.left,node.right = node.right,node.left
            bfs(node.left)
            bfs(node.right)
            return
        bfs(r)
        return root
    
    # 파이썬다운 방식
    if root:
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
    return None
