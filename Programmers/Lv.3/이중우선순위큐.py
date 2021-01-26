
# 힙을 사용하지 않은 일반적인 방법으로 푼 것입니다.
def solution(operations):
    answer = []
    lst=[]
    for operation in operations:
        direct, num = operation.split()
        if direct=='I':
            lst.append(int(num))
        elif direct=='D' and lst:
            if num=='1':
                lst.remove(max(lst))
            elif num=='-1':
                lst.remove(min(lst))
    if not lst:
        answer=[0,0]
    else:
        answer=[max(lst), min(lst)]
    return answer