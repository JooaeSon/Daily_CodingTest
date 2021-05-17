def f(n):
    bit_length = n.bit_length()

    if not n & 1:
        return n | 1
    if not (n+1) & n:
        return (n | (n+1)) ^ (1 << (bit_length-1))
    for i in range(bit_length):
        if (1 << i) | n != n:
            n |= (1 << i)
            n ^= (1 << (i-1))
            return n

def solution(numbers):
    return [f(x) for x in numbers]

# 참조: https://blog.hoony.me/3