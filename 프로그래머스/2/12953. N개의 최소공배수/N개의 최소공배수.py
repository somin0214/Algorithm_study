
# 2 수의 최대 공약수 구하기
def solution1(a, b):

    answer = 0
    a, b = int(min(a, b)), int(max(a, b))


    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            answer = i

    return answer


def solution(arr):

    # 최소 공배수는 두 수의 곱/최대공약수
    answer = 1
    for i in arr:
        a = solution1(i, answer) # 두 수의 최대 공약수
        answer = i * answer // a



    return answer