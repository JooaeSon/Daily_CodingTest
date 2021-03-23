N = int(input())
lst=[int(input()) for _ in range(N)]

lst.sort()
for i in range(len(lst)):
    print(lst[i])