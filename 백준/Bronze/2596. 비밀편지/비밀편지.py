n = int(input())
data = input()
res = ""
def h(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))
cod = {
    'A': "000000",
    'B': "001111",
    'C': "010011",
    'D': "011100",
    'E': "100110",
    'F': "101001",
    'G': "110101",
    'H': "111010"
}
for i in range(n):
    chu = data[i*6:(i+1)*6]
    fou = False
    for ch, code in cod.items():
        if h(chu, code) <= 1:
            res += ch
            fou = True
            break
    if not fou:
        print(i + 1)
        break
else:
    print(res)