from collections import defaultdict

N = int(input())
lst=[list(map(int, input().split())) for _ in range(N**2)]
dict = defaultdict(list)
classRoom=[[0 for _ in range(N)] for _ in range(N)]
ans=0

for i in range(len(lst)):
    dict[lst[i][0]].extend(lst[i][1:])

print(dict)     


# 만족도 구하기
'''
for i in range(len(classRoom)):
    for j in range(len(classRoom)):
        classRoom[i][j]
        '''
print(ans)
