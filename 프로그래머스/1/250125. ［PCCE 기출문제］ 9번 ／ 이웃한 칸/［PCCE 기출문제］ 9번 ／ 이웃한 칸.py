def solution(board, h, w):
    # 좌표값 더하는 방법
    # 위 [-1, 0], 아래 [1, 0], 왼쪽 [-1, -1], 오른쪽[0, 1]
    # 단 모든 인덱스는 0 이상 n 미만이어야 함
    answer = 0
    n = len(board) # 2차원 리스트의 길이
    dh = [0, 1, -1, 0] # 행, 높이
    dw = [1, 0, 0, -1] # 열, 너비
    
    for i in range(len(dh)):
        h_check= h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n and board[h][w] == board[h_check][w_check]:
            answer += 1
    
    return answer