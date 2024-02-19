X = int(input())
Stick=64
ans=0

while True:
    if Stick<=X:
        break
    Stick=Stick//2
    Stick+=X
    ans+=1

print(ans)