s='fkdhtshmrw4nxg#f44ehlbn33ccto#mwfn2waebry#3qd1ubwyhcyuavuajb#vyecsycuzsmwp31ipzah#catatja3kaqbcss2th'
cnt = 0
n = len(s)

for i in range(n):
    num = 0
    sym = 0
    for j in range(i,n):
        c = s[j]
        if c.isdigit():
            num += 1
        elif not c.isalpha():
            sym += 1
            #子串长度公式
        if j - i + 1 > 16:
            break
        if j - i + 1 >= 8 and num >= 1 and sym >= 1:
            cnt += 1
print(cnt)