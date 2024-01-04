def solution(s):
    x = 0
    y = 0
    while s != '1':
        y += s.count('0') 
        a = s.count('1')
        s = bin(a)[2:]
        x += 1
    return [x, y]