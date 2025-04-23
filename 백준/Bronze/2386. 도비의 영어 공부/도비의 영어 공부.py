while True:
    l = input()
    if l == '#':
        break
    ch, sentence = l[0], l[2:]
    count = sentence.lower().count(ch)
    print(f"{ch} {count}")