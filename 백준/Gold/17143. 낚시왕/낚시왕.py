import sys
input = sys.stdin.readline
R,C,M = map(int, sys.stdin.readline().split())
if M == 0:
    print(0)
    sys.exit()
sharkinfo = [list(map(int, input().split())) for _ in range(M)]
pan = [[[] for i in range(C)] for _ in range(R)]
shark = []
while sharkinfo:
    r,c,s,d,z = sharkinfo.pop()
    pan[r-1][c-1].append([s,d,z])
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
# 낚시왕 이동
for i in range(C):
    for j in range(R):
        if pan[j][i]:
            s,d,z = pan[j][i].pop()
            result += z
            break
    for j in range(R):
        for k in range(C):
            if pan[j][k]:
                s,d,z=pan[j][k].pop()
                shark.append([j,k,s,d,z])
    while shark:
        j, k, s, d, z = shark.pop()
        if d == 1 or d == 2:
            cycle = (R-1)*2
            move = s % cycle
            if d == 1:
                if move <= j:
                    nj = j - move
                    nd = 1
                else:
                    move -= j
                    if move <= R-1:
                        nj = move
                        nd = 2
                    else:
                        nj = 2*(R-1) - move
                        nd = 1
            else:
                if move <= R-1-j:
                    nj = j + move
                    nd = 2
                else:
                    move -= (R-1-j)
                    if move <= R-1:
                        nj = R-1 - move
                        nd = 1
                    else:
                        nj = move - (R-1)
                        nd = 2
            nk = k
        else:
            cycle = (C-1)*2
            move = s % cycle
            if d == 4:
                if move <= k:
                    nk = k - move
                    nd = 4
                else:
                    move -= k
                    if move <= C-1:
                        nk = move
                        nd = 3
                    else:
                        nk = 2*(C-1) - move
                        nd = 4
            else:
                if move <= C-1-k:
                    nk = k + move
                    nd = 3
                else:
                    move -= (C-1-k)
                    if move <= C-1:
                        nk = C-1 - move
                        nd = 4
                    else:
                        nk = move - (C-1)
                        nd = 3
            nj = j
        pan[nj][nk].append([s, nd, z])
    for j in range(R):
        for k in range(C):
            if len(pan[j][k])>=2:
                pan[j][k].sort(key=lambda x:-x[2])
                while len(pan[j][k])>1:
                    pan[j][k].pop()
print(result)