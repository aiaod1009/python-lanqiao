#我的写法
S = input().strip()
T = input().strip()
i = 0
cnt = 0
idx = 0
while i < len(T):
    found = False
    for j in range(idx, len(S)):
        if T[i] == S[j]:
            cnt += 1
            idx = j + 1
            found = True
            break  # 找到就跳出，避免无效遍历
    if not found:  # 没找到，直接终止循环
        break
    i += 1
print(cnt)


#更好的写法
S = input().strip()
T = input().strip()
i = j = 0
while i < len(S) and j < len(T):
    if S[i] == T[j]:
        j += 1
    i += 1
print(j)