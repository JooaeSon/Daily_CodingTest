from itertools import combinations

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    for i in range(2, x):
  	    # x가 해당 수로 나누어떨어지면
        if x % i == 0:
    	    return False
    return True

def solution(nums):
    answer=0
    lst=list(combinations(nums, 3))
    #print(lst)
    for l in lst:
        if is_prime_number(sum(l)):
            answer+=1

    return answer