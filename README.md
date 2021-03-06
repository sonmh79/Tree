# 트리에 대해 알아보자
참조 '파이썬 알고리즘 인터뷰-저자 박상길'  

## 개념

트리는 계층형 트리 구조를 시뮬레이션 하는 **추상 자료형(ADT)** 으로,  
루트 값과 부모-자식 관계의 **서브트리**로 구성되며, 서로 연결된 노드의 집합이다.

![이진트리](https://dbscthumb-phinf.pstatic.net/3523_000_1/20141020113417790_HOLB9ZB8H.jpg/ka7_119_i5.jpg?type=w340_fst&wm=N)

## 특징
### 추상형 자료구조(ADT)

-위에서 아래로 뻗어나가는 개념을 컴퓨터로 개념화 시킨 형태
### 부모-자식 관계의 서브트리

- 부모도 트리이고 자식도 트리 

- 재귀로 정의된 자기참조 자료구조라고도 말한다

## 명칭
이름 | 설명
:--:|:--:
루트(root) |  시작, 뿌리
자식(child) | 부모는 자식을 가진다
간선(edge) | 부모와 자식 연결
차수(degree) | 자식 노드의 개수  
크기(Size) | 자신을 포함한 모든 노드의 개수
높이(height) | 현재 위치에서 leaf까지 거리
깊이(depth) | 루트에서부터 현재노드까지 거리

## 그래프와 차이점
### 트리는 그래프의 일부, but
1. 트리는 오직 단방향이다.  
2. 하나의 부모 노드를 갖는다.  
3. 순환 구조를 갖지 않는다.  



## 이진 트리는?
- 다항(다진) 트리(m-ary): 각 노드가 m개 이하의 자식을 가지고 있음
- 이진 트리(Binary Tree): m = 2인 트리, 모든 노드의 차수가 2이하

트리 | 설명
:--:|:--:
정 이진 트리(Full) | 0~2개의 자식 노드
완전 이진 트리(Complete) | 마지막 레벨을 제외하고 왼쪽부터 채워진 노드
포화 이진 트리(Perfect) | 모든 노드가 2개의 자식을 가짐


# 이진 탐색 트리(BST)
- 노드의 왼쪽 오른쪽 값들이 크기에 따라 정렬되어 있는 트리
- 시간 복잡도 O(log n) , 매우 효율적인 트리
- 불균형 트리(비효율적인 트리)는 시간 복잡도 최대 O(n)

자가 균형 이진 탐색 트리는 삽입, 삭제 시 자동으로 높이를 작게 유지하는 노드 기반 이진 탐색 트리이다.
 - AVL트리, 레드-블랙 트리 등
 
# 트리 순회(Tree Traversals)
## 전위, 중위, 후위 순회 재귀 코드
N: 현재 L: 왼쪽 R: 오른쪽
```Python
#전위 순회 #NLR
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# 중위 순회 #LNR
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
    
# 후위 순회 #LRN
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
```
