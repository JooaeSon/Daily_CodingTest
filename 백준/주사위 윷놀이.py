# 다음에 갈 좌표
guide = [0]*33
for i in range(21):
    guide[i]=i+1

guide[21]=21
guide[22], guide[23], guide[24] = 23, 24, 30
guide[25], guide[26] = 26, 30
guide[27], guide[28], guide[29] = 28, 29, 30
guide[30], guide[31], guide[32] = 31, 32, 20

blueZone=[i for i in range(16)]
blueZone[5], blueZone[10], blueZone[15] = 22, 25, 27

# 얻어갈 점수
plus = [0]*33
for i in range(21):
    plus[i]=i*2

plus[22], plus[23], plus[24] = 13, 16, 19
plus[25], plus[26] = 22, 24
plus[27], plus[28], plus[29] = 28, 27, 26
plus[30], plus[31], plus[32] = 25, 30, 35


dice = list(map(int, input().split()))
horse=[0 for _ in range(4)]
chk=[0 for _ in range(33)]


def dfs(dice_idx, point):
    global max_ans

    if dice_idx>=10:
        max_ans=max(point, max_ans)
        return

    for i in range(4):
        curr, move = horse[i], dice[dice_idx] # 말 위치, 주사위 번호
        pre=curr

        if curr==5 or curr==10 or curr==15:
            curr=blueZone[curr]
            move-=1

        if curr+move <= 21:
            curr+=move
        else:
            for _ in range(move): # 한칸씩 움직임
                curr=guide[curr]

        if chk[curr] and curr!=21:
            continue

        chk[pre], chk[curr], horse[i]=0, 1, curr
        dfs(dice_idx+1, point+plus[curr])
        chk[pre], chk[curr], horse[i] = 1, 0, pre


max_ans=0
dfs(0, 0)
print(max_ans)

# 참조:https://chldkato.tistory.com/133