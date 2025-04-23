btn = [300, 60, 10]
cnt = []
t = int(input())
for i in range(3):
    bCnt = t // btn[i]
    t %= btn[i]
    cnt.append(bCnt)
if t == 0:
    for c in cnt:
        print(c, end=' ')
else:
    print(-1)