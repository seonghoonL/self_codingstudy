N = int(input())
touches = [set(map(int, input().split())) for _ in range(N)]
required = [set([1, 3]), set([3, 4]), set([1, 4])]
required_set = set(map(frozenset, required))
given_set = set(map(frozenset, touches))
bad_fingers = any(2 in pair or 5 in pair for pair in given_set)
if required_set.issubset(given_set) and not bad_fingers:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")