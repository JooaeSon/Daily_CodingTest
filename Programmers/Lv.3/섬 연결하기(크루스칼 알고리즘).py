parent = dict()  # 부모 정보
rank = dict()  # 자기자신을 포함한 조상의 수


# node 초기화
def make_set(node):
    parent[node] = node  # 처음 부모는 자기 자신
    rank[node] = 0


# 최상 부모노드 찾기
def findParent(node):
    if parent[node] != node:  # 자기 자신이 아니라면
        parent[node] = findParent(parent[node])  # 제일 최상 부모를 찾을 때까지 재귀호출

    return parent[node]


# 합치기
def union(n1, n2):
    # 각 노드 마다 최상위 부모 찾기
    root1 = findParent(n1)
    root2 = findParent(n2)
    if root1 != root2:  # 루트 값이 다르면 다른 집합
        if rank[root1] > rank[root2]:  # 노드 수가 적은 집합의 루트가 노드 수가 많은 집합의 루트로 변경됨
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:  # 각 집합의 개수가 같다면
                rank[root2] += 1  # 둘중 아무노드 집합 하나 늘려주기


# 크루스칼 알고리즘 사용
def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 가중치 오름차순으로 정렬

    for i in range(n): make_set(i)
    value = 0
    for cost in costs:
        n1, n2, v = cost[0], cost[1], cost[2]
        if findParent(n1) != findParent(n2):  # 서로의 부모가 다르다면
            union(n1, n2)  # 서로를 연결한다.
            value += v  # 해당 비용 더해주기

    return value