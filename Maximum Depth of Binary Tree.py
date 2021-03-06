# Leet code 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 예외처리!!
        if root is None:
            return 0

        # 큐
        queue = collections.deque([root])
        depth = 0

        # BFS
        # depth만큼 반복
        while queue:
            depth += 1
            # 큐에서 추출한 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return depth