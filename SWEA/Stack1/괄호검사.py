T = int(input())

for test_case in range(1, T + 1):
    result = 0
    stack = list(input())
    temp = []

    while stack:
        value = stack.pop()
        if value == '{' or value == '}' or value == '(' or value == ')':
            if len(temp) == 0:
                temp.append(value)
            else:
                if value == '{' and temp[-1] == '}':
                    temp.pop()
                elif value == '(' and temp[-1] == ')':
                    temp.pop()
                else:
                    temp.append(value)
        #print("stack", stack)
        #print("temp", temp)
    else:
        if '{' in temp or '}' in temp or '(' in temp or ')' in temp:
            result = 0
        else:
            result = 1
    print(f'#{test_case} {result}')
