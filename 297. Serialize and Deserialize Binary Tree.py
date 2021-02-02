# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #직렬화
        #예외 처리
        if root is None:
            return []
        queue = collections.deque([root])
        result = ['#']
        
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            
                result.append(str(node.val))
            else:
                result.append('#')
            
        return result

    def deserialize(self, data):
        # 음수를 문자열로 만들면 부호 - 와 숫자 분리됨
        # 그래서 인풋을 리스트로 받음
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #역직렬화
        #예외처리
        if data == []:
            return None

        #두번째 인덱스부터 뿌리 노드 설정
        root = TreeNode(data[1])
        queue = collections.deque([root])
        
        #인덱스로 자식 노드 붙여주기
        index = 2
        while queue:
            node = queue.popleft()
            if data[index] is not '#':
                node.left = TreeNode(data[index])
                queue.append(node.left)
            index +=1
            
            if data[index] is not '#':
                node.right = TreeNode(data[index])
                queue.append(node.right)
            index += 1
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
