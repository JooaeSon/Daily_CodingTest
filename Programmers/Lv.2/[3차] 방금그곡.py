def cal_time(start_time, end_time):
    total = 0

    hour = int(end_time.split(':')[0]) - int(start_time.split(':')[0])
    minute = int(end_time.split(':')[1]) - int(start_time.split(':')[1])

    if hour > 0:
        total += hour * 60
    total += minute

    return total


def played_sound(sound_lst, play_time):  # 원래 악보, 재생된 시간

    return sound_lst * (play_time // len(sound_lst)) + sound_lst[:play_time % len(sound_lst)]


def chmode_sharp(sound):
    sound_lst = []

    for i in range(len(sound) - 1):
        if sound[i] == '#':
            if sound[i + 1] != '#' and i + 1 == len(sound) - 1:
                sound_lst.append(sound[i + 1])
            continue
        if sound[i + 1] == '#':
            sound_lst.append(sound[i] + sound[i + 1])
        else:
            sound_lst.append(sound[i])
            if i + 1 == len(sound) - 1:
                sound_lst.append(sound[i + 1])
    return sound_lst


def chkInclude(m, melody):
    m_lst = chmode_sharp(m)
    for i in range(len(melody) - len(m_lst) + 1):
        cnt = 0
        for j in range(len(m_lst)):
            if m_lst[j] == melody[i + j]:
                cnt += 1
        if cnt == len(m_lst):
            return True

    return False


def solution(m, musicinfos):
    answer = ''
    change_musicinfos = []
    # 시간 차(분 단위)를 구한 다음 악보정보를 그만큼 계산
    for i in range(len(musicinfos)):
        musicinfos[i] = list(musicinfos[i].split(","))
        start_time = musicinfos[i][0]
        end_time = musicinfos[i][1]
        # 재생된 시간 구하기
        play_time = cal_time(start_time, end_time)
        sound_lst = chmode_sharp(musicinfos[i][3])
        # 재생된 시간 악보 구하기
        musicinfos[i][3] = played_sound(sound_lst, play_time)

    # m과 일치하는 음 정보 찾기
    lst = []
    for idx, musicinfo in enumerate(musicinfos):
        if chkInclude(m, musicinfo[3]):
            lst.append([idx, len(musicinfo[3]), musicinfo[2]])

    # 만약 일치하는 음악 이 여러개일 경우 재생시간이 제일 긴 음악 반환
    # 재생시간도 같은 경우에는 먼저 입력된 음악 먼저
    if len(lst) != 0:
        lst = sorted(lst, key=lambda x: (-x[1], x[0]))
        return lst[0][2]
    # 조건이 일치하는 음악이 없을 경우에는 (None)을 반환
    return '(None)'