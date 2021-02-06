def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and k > 0 and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)