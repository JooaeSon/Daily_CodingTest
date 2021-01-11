import copy

T = int(input())
""""
3
ABCCB
NNNASBBSNV  NANV
UKJWHGGHNFTCRRCTWLALX
"""
for test_case in range(1, T + 1):
    stack = []
    q = list(input())

    while True:
        while len(q) != 0:
            value = q.pop(0)
            if len(q) != 0 and value == q[0]:
                q.pop(0)
            else:
                stack.append(value)
        q = copy.deepcopy(stack)
        stack.clear()

        if len(q) != 0:
            for i in range(len(q)-1):
                if q[i] == q[i+1]:
                    break
            else:
                break

    print(f'#{test_case} {len(q)}')
