s = input().strip()
a = [0 for _ in range(26)]
if len(s) % 2 != 0:
    print('NO')
else:
    for i in s:
        a[ord(i) - ord('a')] += 1
    # for j in range(26):
    #     if a[j] % 2 == 0:
    #         a[j] = 1
    #     else:
    #         a[j] = 0
    # print("YES") if all(a) == 1 else print("NO")
    if all(j % 2 == 0 for j in a):
        print("YES")
    else:
        print("NO")