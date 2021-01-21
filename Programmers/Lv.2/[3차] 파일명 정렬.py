def slice_three(file):
    HEAD = []
    NUMBER = []
    flag = 0
    # 첫번째 문자부분은 대소문자를 구분하지 않는다.
    # 숫자 부분의 앞의 0은 무시된다.
    for i in range(len(file)):
        if (not file[i].isdigit() and flag != 0) or (file[i].isdigit() and flag == 5):
            break

        if not file[i].isdigit() and flag == 0:
            HEAD.append(file[i])
        elif file[i].isdigit():
            NUMBER.append(file[i])
            flag += 1

    return ''.join(HEAD).lower(), int(''.join(NUMBER))


def solution(files):
    file_info = []

    # 파일명을 세부분으로 분류한다.
    for idx, file in enumerate(files):
        head, number = slice_three(file)
        file_info.append((head, number, idx))

    # head 부분과 number의 숫자가 같을 경우, 원래 입력에 주어진 순서를 유지한다.
    file_info = sorted(file_info, key=lambda x: (x[0], x[1], x[2]))

    return [files[file_info[i][2]] for i in range(len(file_info))]