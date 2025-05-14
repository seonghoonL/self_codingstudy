while True:
    num = input().strip()
    if num == '0':
        break
    width = 0
    for digit in num:
        if digit == '1':
            width += 2
        elif digit == '0':
            width += 4
        else:
            width += 3
    width += len(num) - 1
    width += 2
    print(width)