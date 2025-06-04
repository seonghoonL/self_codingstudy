scores = [int(input()) for _ in range(5)]
adjusted = [score if score >= 40 else 40 for score in scores]
print(sum(adjusted) // 5)