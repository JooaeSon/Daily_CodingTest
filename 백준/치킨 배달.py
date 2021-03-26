from itertools import combinations

N, M = map(int, input().split())
city=[list(map(int, input().split())) for _ in range(N)]

store=[]
house=[]

for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append((i, j))
        elif city[i][j]==2:
            store.append((i, j))


selected=list(combinations(store, M))

# 각각의 집과 가장 가까운 치킨집 사이 거리를 계산
min_dist=float('inf')
for chicken_comb in selected:
    dist=0
    for h in house:
        Min=float('inf')
        for ck in chicken_comb:
            Min=min(Min, abs(h[0]-ck[0])+abs(h[1]-ck[1]))
        dist+=Min
    min_dist=min(min_dist, dist)

# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.
print(min_dist)
