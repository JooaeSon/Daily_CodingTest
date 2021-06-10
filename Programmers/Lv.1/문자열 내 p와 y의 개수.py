def solution(s):
    s=s.upper()
    if s.count("P")!=s.count("Y"):
        answer = False
    else:
        answer=True

    return answer