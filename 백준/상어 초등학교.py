from collections import defaultdict
'''
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

'''
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

for std, like_std in dict.items():
    print("std:", std)
    print("like_std: ", like_std)
    # 인접한 칸에 좋아하는 학생들이 많은 칸 고르기
    seat = []
    for i in range(N):
        for j in range(N):
            like, blank= 0, 0
            if not classRoom[i][j]: # 빈칸이라면
                for dir in range(4): # 사방을 탐색하여 좋아하는 학생이 있는지 찾는다.
                    nx, ny=i+dx[dir], j+dy[dir]
                    if 0<=nx<N and 0<=ny<N:
                        if classRoom[nx][ny]: # 인접한 자리가 빈칸이 아닐때 좋아하는 사람이 있는지 확인
                            if classRoom[nx][ny] in like_std:
                                like+=1
                        else: # 빈칸일 때
                            blank+=1

                seat.append((like, blank, i, j))
                seat=sorted(seat, key=lambda x: (-x[0], -x[1], x[2], x[3]))
                classRoom[seat[0][2]][seat[0][3]]=std
    print(seat)
    print("classRoom: ", classRoom)




# 만족도 구하기
'''
for i in range(N):
    for j in range(N):
        classRoom[i][j]
'''
print(ans)
