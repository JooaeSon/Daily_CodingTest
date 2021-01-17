def win(x, y):
    if (lst[x-1] == 1 and lst[y-1] == 3) or (lst[x-1] == 1 and lst[y-1] == 1):
        return x
    elif (lst[x-1] == 2 and lst[y-1] == 1) or (lst[x-1] == 2 and lst[y-1] == 2):
        return x
    elif (lst[x-1] == 3 and lst[y-1] == 2) or (lst[x-1] == 3 and lst[y-1] == 3):
        return x
    return y

def match(start, end):

    if start == end:
        return start

    first_value = match(start, (start+end)//2)
    second_value = match((start+end)//2+1, end)
    return win(first_value, second_value)

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    start = 1
    end = N
    print(f'#{tc} {match(start, end)}')