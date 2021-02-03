class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        graph = collections.defaultdict(list)
        
        #양방향 그래프
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        while n >2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # 리프 노드 양방향 제거
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        #최종 이웃의 개수가 1인 노드들만 남음(그래프의 중앙)
        return leaves
