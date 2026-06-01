import sys
# data = sys.stdin.read().split()
with open('words.txt', 'r', encoding='utf-8') as f:
    data = [line.strip() for line in f if line.strip()]
data.sort(key=lambda s:len(s))


my_set = set()
ans = ''
for s in data:
    if len(s) == 1 or ''.join(sorted(s[:-1])) in my_set:
        my_set.add(''.join(sorted(s)))
        if not ans or len(s) > len(ans) or ans > s:
            ans = s
print(ans)