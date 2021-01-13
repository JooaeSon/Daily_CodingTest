T = int(input())

for test_case in range(1, T + 1):
    cal = list(input().split())
    num_stack = []
    message = ''
    flag = 0

    for i in range(len(cal)-1):
        if cal[i].isdigit():
            num_stack.append(cal[i])
        else:
            try:
                n2 = int(num_stack.pop())
                n1 = int(num_stack.pop())
                result = 0
                if cal[i] == '+':
                    result = n1 + n2
                elif cal[i] == '*':
                    result = n1 * n2
                elif cal[i] == '-':
                    result = n1 - n2
                elif cal[i] == '/':
                    result = n1 // n2
                num_stack.append(str(result))
            except:
                flag = 987654321

    if flag == 0 and len(num_stack) == 1:
        message = str(num_stack[0])
    elif flag == 987654321 or len(num_stack) != 1:
        message = 'error'

    print(f'#{test_case} {message}')
