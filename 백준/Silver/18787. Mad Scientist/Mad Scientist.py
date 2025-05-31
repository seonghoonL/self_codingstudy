n = int(input())
a = input()
b = input()
result = 0
flag = False
for i in range(len(b)) :
  if flag == True or a[i] != b[i] :
    flag = True
  if flag == True and a[i] == b[i] :
    result += 1
    flag = False
print(result)