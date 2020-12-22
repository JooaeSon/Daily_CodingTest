import itertools
import math

# 제곱근까지만 보고 소수를 판별하는 함수
def is_prime_number(x):
    if x==0 or x==1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers=list(numbers)
    num_set=set()
    for i in range(1, len(numbers)+1):
        lst=list(itertools.permutations(numbers, i))
        for l in lst:
            if is_prime_number(int(''.join(l))):
                num_set.add(int(''.join(l)))
    return len(num_set)