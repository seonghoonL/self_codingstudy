n = int(input())
total_left = 0
for _ in range(n):
    students, apples = map(int, input().split())
    total_left += apples % students
print(total_left)