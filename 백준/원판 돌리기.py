import sys
from collections import deque

N, M, T = map(int, input().split())
roundPlate=[deque(map(int, input().split())) for _ in range(N)]
rotate_info = [list(map(int, input().split())) for _ in range(T)]

same=0
def adjacent(RP):
    global same, roundPlate, tmp

    tmp=RP
    same = 0
    # 가로 인접
    for i in range(len(RP)):
        for j in range(M):
            if j==M-1:
                j = -1
            if RP[i][j]!=-1 and RP[i][j]==RP[i][j+1]: # 같은 수 체크
                tmp[i][j]=-1
                tmp[i][j+1]=-1
                same+=1

    # 세로 인접
    for j in range(M):
        for i in range(len(RP)-1):
            if RP[i][j]!=-1 and RP[i][j]==RP[i+1][j]: # 같은 수 체크
                tmp[i][j]=-1
                tmp[i+1][j]=-1
                same+=1
    roundPlate=tmp

    if same!=0: return True
    else: return False


def Sum(roundPlate):
    ssum, n = 0, 0
    rp = sum(roundPlate, deque())
    for i in range(len(rp)):
        if rp[i]!=-1:
            n+=1
            ssum+=rp[i]
    return ssum, n


# 원판 돌리기
for info in rotate_info:
    x, d, k = info[0], info[1], info[2]
    cnt=1
    num=x
    while num<=len(roundPlate): # x 배수 회전
        if d==0: # 시계 방향
            roundPlate[num-1].rotate(k)
        else: # 반시계 방향
            roundPlate[num-1].rotate(-k)
        cnt+=1
        num = x * cnt
    # 다 돌린 후 원판에 수가 남아있는지 확인하고 인접한 수 있는지 확인
    chk=sum(roundPlate, deque())
    if chk.count(-1)==len(chk): # 남아 있는 수가 없음
        print(0)
        sys.exit() # 종료

    # 인접한 수 확인
    tmp = []
    if not adjacent(roundPlate):
        # 없으면 원판에 적힌 수 평균 구하고 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
        ssum, n = Sum(roundPlate)
        avg=ssum/n
        for i in range(len(roundPlate)):
            for j in range(M):
                if roundPlate[i][j]!=-1:
                    if roundPlate[i][j]>avg:
                        roundPlate[i][j]-=1
                    elif roundPlate[i][j]< avg:
                        roundPlate[i][j]+=1

# 다 돌린 후 원판의 최종 합 구하기
result_sum, result_n =Sum(roundPlate)

print(result_sum)