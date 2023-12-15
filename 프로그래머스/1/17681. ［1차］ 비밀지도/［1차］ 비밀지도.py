def solution(n, arr1, arr2):
    answer = []
    arr12 = []
    arr22 = []
    s = ''
    
    # 이진법으로 만들어서 리스트에 넣기 
    for i, j in zip(arr1, arr2):
        a = bin(i)[2:]
        b = bin(j)[2:]
        arr12.append(a)
        arr22.append(b)
    
    for i in range(n):
        m = len(arr12[i])
        if m != n:
            new = '0'*(n-m) + arr12[i]
            arr12[i] = new
            
    for i in range(n):
        m = len(arr22[i])
        if m != n:
            new = '0'*(n-m) + arr22[i]
            arr22[i] = new
    
    
    for i in range(n):
        for j in range(n):
            if arr12[i][j] == '1' or arr22[i][j] == '1':
                s += '#'
            else:
                s += ' '
        answer.append(s)
        s = ''
    print(arr12, arr22)

    return answer