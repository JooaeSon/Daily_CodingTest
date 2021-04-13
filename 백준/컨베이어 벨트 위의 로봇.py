from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))
robot = deque([0]*(N*2))
ans=1

while True:
    # 1 밸트 한 칸씩 회전
    A.rotate(1)
    robot.rotate(1)
    robot[N-1]=0 # 땅으로 내려감

    # 2 로봇의 이동
    for i in range(N-2, -1, -1):
        if robot[i]==1 and robot[i+1]==0 and A[i+1]>=1:
            robot[i+1]=robot[i]
            robot[i]=0
            A[i+1]-=1
    robot[N-1]=0

    # 3 로봇 올리기
    if robot[0]==0 and A[0]!=0: # 올라가는 위치에 로봇이 없다면
        robot[0]=1 # 로봇을 올린다.
        A[0]-=1

    # 4 종료 조건 따지기
    cnt=0
    for i in range(len(A)):
        if A[i]==0:
            cnt+=1

    if cnt >= K: # 내구도가 0인 칸의 개수가 k개 이상이면 과정을 종료
        break

    ans+=1

print(ans)


