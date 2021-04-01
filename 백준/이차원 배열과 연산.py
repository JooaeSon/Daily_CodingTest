r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def sorting(lst):
    lst.sort()
    if 0 in lst: # 0을 무시하기 위해
        while 0 in lst:
            lst.remove(0)

    dict={}
    for key in set(lst):
        dict[key]=0

    while lst:
        value=lst.pop()
        if value in dict:
            dict[value]+=1
    tmp=[]
    for key, value in dict.items():
        tmp.append((key, value))
    tmp.sort(key=lambda x: (x[1], x[0]))

    result=[]
    for t in tmp:
        result.append(t[0])
        result.append(t[1])

    return result

def makeArray(A_tmp):
    length=[]
    for i in range(len(A_tmp)):
        length.append(len(A_tmp[i]))
    Max_length = max(length)

    for i in range(len(length)):
        if Max_length > length[i]:
            A_tmp[i].extend([0]*(Max_length-length[i]))

    return A_tmp

time=0
while True:
    R, C = len(A), len(A[0])

    if (0<=r-1<R and 0<=c-1<C) and A[r-1][c-1]==k:
        break
    if time>100:
        time = -1
        break

    if R >= C: # R 연산 적용
        A_tmp=[]
        for i in range(R):
            A_tmp.append(sorting(A[i]))
        A=makeArray(A_tmp)
    else: # C 연산 적용
        sero_A=[]
        for a in zip(*A): # 잠시 열을 계산하기 위해 교차
            sero_A.append(list(a))
        A_tmp = []
        for i in range(C):
            A_tmp.append(sorting(sero_A[i]))
        sero_A = makeArray(A_tmp)

        garo_A=[]
        for a in zip(*sero_A): # 계산이 끝난후 다시 처음으로 리셋
            garo_A.append(list(a))
        A=garo_A

    time+=1


print(time)