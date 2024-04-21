target = int(input())
ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())

if M:
    broken = list(input().split())
else:
    broken = list()

'''
0-9까지 숫자 있음
+: 채널 +1
-: 채널 -1
채널 0에서 -를 누른 경우 채널이 변하지 않고 채널은 무한대 만큼 있다

n(0<=n<=500000) 채널로 이동하려고 함.
어떤 버튼이 고장 났는지가 주어졌을 때, 채널 n으로 이동하기 위해 버튼을 최소 몇번 눌러야 하는가?

현재 보고 있는 채널은 100
'''

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001):
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)

'''참조: https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-1107-%EB%A6%AC%EB%AA%A8%EC%BB%A8
'''