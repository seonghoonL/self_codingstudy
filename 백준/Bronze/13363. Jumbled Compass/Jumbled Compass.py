import sys
input = sys.stdin.readline
n1 = int(input())
n2 = int(input())
diff = (n2 - n1) % 360
if diff == 180:
    print(180)
elif diff > 180:
    print(diff - 360)
else:
    print(diff)