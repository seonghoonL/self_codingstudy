S1, S2 = map(int, input().split())
sample_correct = True
system_correct = True
for _ in range(S1):
    ans, user = map(int, input().split())
    if ans != user:
        sample_correct = False
for _ in range(S2):
    ans, user = map(int, input().split())
    if ans != user:
        system_correct = False
if not sample_correct:
    print("Wrong Answer")
elif not system_correct:
    print("Why Wrong!!!")
else:
    print("Accepted")