n = int(input())
votes = [int(input()) for _ in range(n)]
if votes[0] == max(votes) and votes.count(max(votes)) == 1:
    print('S')
elif votes[0] == max(votes):
    print('S')
else:
    print('N')