while True:
    line = input()
    if line == "#":
        break
    reversed_words = [word[::-1] for word in line.split()]
    print(' '.join(reversed_words))