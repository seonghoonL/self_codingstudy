def solve(r, n):
    if n == 0:
        return r
    if n%9:
        return solve(str(n%9)+r, n//9)
    else:
        return solve("0"+r, n//9)
print(solve("", int(input())))