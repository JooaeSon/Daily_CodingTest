X = int(input())
Stick=64
ans=0

while X>0:
    if Stick > X:
        Stick=Stick//2
    else:
        X-=Stick
        ans+=1

print(ans)