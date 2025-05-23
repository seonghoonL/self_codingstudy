def solution(input_list):
    answer = []
    for t in range(len(input_list)):
        num = 0
        left_count = 0
        right_count = 0
        is_right = False
        for i in input_list[t]:
            if is_right:
                if i == "!":
                    right_count += 1
            elif i == "!":
                left_count += 1
            elif i.isdigit():
                num = int(i)
                is_right = True
        if right_count >= 1:
            num = 1
        if (left_count % 2) != 0:
            num = 1 - num
        answer.append(num)
    for a in answer:
        print(a)
    return
T = int(input())
input_list = []
for _ in range(T):
    t = input().strip()
    input_list.append(t)
solution(input_list)