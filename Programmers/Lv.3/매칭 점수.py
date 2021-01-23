import re


def find_external_link(external_link_dic, lp, url):
    s = set()
    for e in re.findall(r'<a href="https://[\S]*">', lp):
        s.add(re.search(r'"https://([\S]*)"', e).group(1))
    external_link_dic[url] = s

    return external_link_dic


def find_search_word(lp, word):
    wordCnt = 0
    for find in re.findall(r'[a-zA-Z]+', lp):
        if find == word.lower():
            wordCnt += 1
    return wordCnt


def solution(word, pages):
    pages_info = {}
    external_link_dic = {}
    # 기본점수: 검색어가 등장하는 횟수(대소문자 무시)
    for idx in range(len(pages)):
        lp = pages[idx].lower()
        url = re.search(r'meta[^>]*content="https://([\S]*)"/>', lp).group(1)
        wordCnt = find_search_word(lp, word)
        pages_info[url] = [idx, wordCnt]

        # 외부 링크 수: 해당 웹페이지에서 다른 외부 페이지로 연결된 링크 개수
        external_link_dic = find_external_link(external_link_dic, lp, url)
        pages_info[url].append(len(external_link_dic[url]))

    # 매칭점수: 기본점수+링크점수
    matchingPoint = []
    for link in pages_info:
        Sum = 0
        # 링크점수: 해당 웹페이지로 링크가 걸린 다른 웹페이지의 (기본점수/외부 링크 수)
        for key, item in external_link_dic.items():
            if link in item:
                Sum += (pages_info[key][1] / pages_info[key][2])

        matchingPoint.append(Sum)

    for page in pages_info:
        matchingPoint[pages_info[page][0]] += pages_info[page][1]

    for idx, point in enumerate(matchingPoint):
        matchingPoint[idx] = (point, idx)

    # 매칭 점수가 제일 높고 점수가 같다면 작은 idx를 구하라
    return sorted(matchingPoint, key=lambda x: (-x[0], x[1]))[0][1]