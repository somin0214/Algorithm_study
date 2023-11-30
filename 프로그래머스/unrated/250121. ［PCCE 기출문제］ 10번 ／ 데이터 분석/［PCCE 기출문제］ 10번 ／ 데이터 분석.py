def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_list = ['code', 'date', 'maximum', 'remain']
    for a in data:
        idx1 = ext_list.index(ext)
        idx2 = ext_list.index(sort_by)
        if a[idx1] < val_ext:
            answer.append(a)
    return sorted(answer, key = lambda x : x [idx2])
