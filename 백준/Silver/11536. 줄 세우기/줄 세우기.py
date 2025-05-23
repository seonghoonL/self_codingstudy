n = int(input())
arr = []
for _ in range(n):
    name = input()
    arr.append(name)
if sorted(arr) == arr:
        print("INCREASING")
elif sorted(arr, reverse=True) == arr:
        print("DECREASING")
else:
        print("NEITHER")