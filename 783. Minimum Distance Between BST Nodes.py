# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        # 재귀 구조 중위 순회 비교
        if root.left:
            self.minDiffInBST(root.left)
        # 이전 노드와 차이 값 계산
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
        return self.result
    
    #반복 구조 중위 순회 비교
    node = root
    stack = []
    while stack or node:
        # 왼쪽으로 끝까지 이동
        while node:
            stack.append(node)
            node = node.left
        # 루트에서 계산    
        node = stack.pop()
        result = min(result,node.val - prev)
        prev = node.val
        # 오른쪽으로 이동
        node = node.right
