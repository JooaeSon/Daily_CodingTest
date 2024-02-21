N = int(input())
infos = []

for _ in range(N):
    age, name = input().split()
    infos.append([int(age), name])

for info in sorted(infos, key=lambda x:x[0]):
    print(info[0], info[1])
