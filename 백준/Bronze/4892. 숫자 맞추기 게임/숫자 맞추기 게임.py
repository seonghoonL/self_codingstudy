case_num = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 0:
        even_odd = 'even'
        n2 = n1 // 2
    else:
        even_odd = 'odd'
        n2 = (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    print(f"{case_num}. {even_odd} {n4}")
    case_num += 1