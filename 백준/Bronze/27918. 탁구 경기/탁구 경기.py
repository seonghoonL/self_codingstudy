n = int(input())
d_score = 0
p_score = 0
for _ in range(n):
    winner = input().strip()
    if winner == 'D':
        d_score += 1
    else:
        p_score += 1
    if abs(d_score - p_score) >= 2:
        break
print(f"{d_score}:{p_score}")