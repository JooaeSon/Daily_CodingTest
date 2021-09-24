from collections import defaultdict

N = int(input())
lst=[list(map(int, input().split())) for _ in range(N**2)]
dict = defaultdict(list)
classRoom=[[0 for _ in range(N)] for _ in range(N)]
ans=0

dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]

for i in range(len(lst)):
    dict[lst[i][0]].extend(lst[i][1:])

print(dict)     

# 가장많은 빈칸인 것 찾기
for i in range(N):
    for j in range(N):
        cnt=0
        if classRoom[i][j]==0:
            for dir in range(4):
                nx, ny=i+dx[dir], j+dy[dir]
                if 0<=nx<N and 0<=ny<N and classRoom[nx][ny]==0:
                    cnt+=1




# 만족도 구하기
'''
for i in range(N):
    for j in range(N):
        classRoom[i][j]
'''
print(ans)
