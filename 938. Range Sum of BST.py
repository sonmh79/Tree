# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    # My Solution
    # 브루트 포스 ㅠㅠ
    # DFS
    # R.T: 320 ms
    # M.U: 22.3 MB
        
        # 루트 노드가 범위 내에 있는지 확인 후 추가
        if low <= root.val <= high:
            self.res += root.val
        else:
            res = 0
        #DFS, 범위 내 노드값 결과에 추가
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            if left and low <= left <= high:
                self.res += left
            right = dfs(node.right)
            if right and low <= right <= high:
                self.res += right
            
            return node.val
        dfs(root)
        return self.res
    #브루트 포스 모범답안
    if not node:
        return 0
    
    return (root.val if low <= root.val <= high else o) + \
            self.rangeSumBST(root.left,low,high) + \
            self.rangeSumBST(root.right,low,high)

    #DFS 가지치기
        def dfs(node:TreeNode):
            if not node:
                return 0
            
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) +dfs(node.right)
