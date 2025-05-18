import sys
input = sys.stdin.readline
R,C,M = map(int, sys.stdin.readline().split()) # 세로 가로 상어의 수
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
        j,k,s,d,z = shark.pop()
        for _ in range(s):
            j = j+dx[d-1]
            k = k+dy[d-1]
            if k<0 or j<0 or j>R-1 or k>C-1:
                if d==1:
                    d=2
                elif d==2:
                    d=1
                elif d==3:
                    d=4
                elif d==4:
                    d=3
                j = j+dx[d-1]
                k = k+dy[d-1] 
                j = j+dx[d-1]
                k = k+dy[d-1] 
        pan[j][k].append([s,d,z])
    for j in range(R):
        for k in range(C):
            if len(pan[j][k])>=2:
                pan[j][k].sort(key=lambda x:-x[2])
                while len(pan[j][k])>1:
                    pan[j][k].pop()
print(result)