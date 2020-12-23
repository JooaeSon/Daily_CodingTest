def solution(s):
    s_lst = list(s.split(" "))
    # print(s_lst)
    for i in range(len(s_lst)):
        s_lst[i] = s_lst[i].capitalize()

    return ' '.join(s_lst)