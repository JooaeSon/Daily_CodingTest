def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    total_time = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        total_time[start] += 1
        total_time[end] -= 1

    #  total_time[i] = 시각 i부터 i+1까지 1초 간의 구간을 포함하는 재생 구간의 개수
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]
    # 0부터 i초 까지의 누적 시청자 수
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    most_view = 0
    max_time = 0
    '''
    반복문을 돌며 시각 i - adv_time + 1에 광고를 넣을 때의 누적 재생 시간을 구하여, 그중에서 가장 긴 시간을 max_time에 넣어주고 있습니다. max_time 값이 마지막으로 업데이트될 때의 시각 i - at + 1을 HH:MM:SS 형태로 변환한 값이 문제에서 요구하는 정답
    '''
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < total_time[i] - total_time[i - adv_time]:
                most_view = total_time[i] - total_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)

    return h + ':' + m + ':' + s