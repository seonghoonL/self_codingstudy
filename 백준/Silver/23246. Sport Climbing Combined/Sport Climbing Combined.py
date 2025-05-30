player = int(input())
input_score = [list(map(int, input().split())) for _ in range(player)]
input_score = sorted(input_score, key=lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))
for i in input_score[:3]:
	print(i[0], end=" ")