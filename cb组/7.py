n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = [B[i] - A[i] for i in range(n)]

max_cnt = 0

for l in range(n):
    for r in range(l, n):
        k = d[l]

        cnt = 0
        for i in range(n):
            if l <= i <= r:
                if d[i] == k:
                    cnt += 1
            else:
                if d[i] == 0:
                    cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)