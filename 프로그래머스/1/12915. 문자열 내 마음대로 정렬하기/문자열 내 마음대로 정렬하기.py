def solution(strings, n):
    answer = []
    answer = sorted(strings)
    answer = sorted(answer, key = lambda x : x[n])
    # 만약에 같으면 전체적인 것 보고 정렬

    return answer