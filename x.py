#!/usr/bin/python
t = [
[10, 20],
[30, 10],
[50, 10],
[65, 10],
]

t = [
[10, 20],
[30, 10],
[40, 5],
[50, 10],
[65, 10]
]
def compress(t):
    cur_idx = 0
    for i in range(len(t)):
        if i == 0: continue
        if t[cur_idx][0] + t[cur_idx][1] == t[i][0]:
            t[cur_idx][1] += t[i][1]
            t[cur_idx+1][0] = t[cur_idx][0] + t[cur_idx][1]
        else:
            t[cur_idx+1] = t[i]
            cur_idx += 1

    return t[:cur_idx+1]


print compress(t)
