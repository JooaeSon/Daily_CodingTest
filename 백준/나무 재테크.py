
n, m, k = map(int, input().split())
YANGBUN_plus = [list(map(int, input().split())) for _ in range(n)] # 양분 값
YANGBUN = [[5]*n for _ in range(n)]
land = [[[] for _ in range(n)] for _ in range(n)] # 각 좌표마다 심겨질 나무 나이를 저장 할 것.

for _ in range(m):
    x, y, age = map(int, input().split()) # 나무 정보 값
    land[x-1][y-1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def possibleBoundary(nx, ny):
    if 0<=nx<n and 0<=ny<n:
        return True
    else: return False


for year in range(k): # k년 반복

    for i in range(n):
        for j in range(n):
            if land[i][j]:
                land[i][j].sort() # 나이 어린 순 부터 정렬
                live_tree, deadtree=[], 0
                for age in land[i][j]:
                    if age <= YANGBUN[i][j]:
                        YANGBUN[i][j]-=age
                        age+=1
                        live_tree.append(age)
                    else:
                        deadtree+=age//2

                YANGBUN[i][j]+=deadtree
                land[i][j]=[]
                land[i][j].extend(live_tree)

    for i in range(n):
        for j in range(n):
            if land[i][j]:
                # 가을
                for age in land[i][j]:
                    if age%5!=0: # 죽은 나무이거나 5의 배수가 아니라면 생략
                        continue
                    for dir in range(8):
                        nx, ny = i+dx[dir], j+dy[dir]
                        if possibleBoundary(nx, ny):
                            land[nx][ny].append(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            YANGBUN[i][j]+=YANGBUN_plus[i][j]

ans=0
# k년 후 나무 개수 구하기
for i in range(n):
    for j in range(n):
        ans += len(land[i][j])

print(ans)

