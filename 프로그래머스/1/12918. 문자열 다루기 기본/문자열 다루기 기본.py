# def solution(s):
    
#     if len(s) == 4 or len(s) == 6:
#         if s.isnumeric():
#             return True
#         else:
#             return False
#     else:
#         return False

def solution(s):
    answer = True
    for i in s:
        if len(s)==4 or len(s)==6:
            if i.isdigit():
                answer=True
            else:
                answer=False
                break
        else:
            answer=False

    return answer