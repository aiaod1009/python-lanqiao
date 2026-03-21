s = list(map(str,input().strip()))
s1 = list(map(str,input().strip()))
cnt = 0
for i in range(len(s)-1):
        if s[i] != s1[i]:
            s1[i] = 'o' if s1[i] == 'o' else '*'
            s1[i+1] = '*' if s1[i+1] == 'o' else 'o'
            cnt += 1
print(cnt)