def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        new = sorted(array[i-1:j])
        answer.append(new[k-1])
    return answer