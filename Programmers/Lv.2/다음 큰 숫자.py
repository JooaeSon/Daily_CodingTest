def solution(n):
    init_count = bin(n)[2:].count('1')

    while True:
        n += 1
        if bin(n)[2:].count('1') == init_count:
            return n