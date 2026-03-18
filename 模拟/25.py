#太暴力了，很慢
# import sys
# input=lambda :sys.stdin.readline().strip()
# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
#
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         for k in range(n):
#             for l in range(m):
#                 if i == k and j == l:
#                     continue
#                 if a[i][j] == a[k][l] and abs(i - k) == abs(j - l):
#                     cnt += 1
# print(cnt)

# By ChenXiJie2013(luogu uid:928418)
def main():
    a = []
    n, m = map(int, input().split())
    zheng, fan = dict(), dict()
    getz, getf = zheng.get, fan.get
    ans = 0
    for i in range(n):
        a.append(tuple(map(int, input().split()))) # 注意map强转成tuple元组代替列表
    for i in range (n):
        for j in range(m):
            # 找键，没有就返回0
            ans += getz((i + j, a[i][j]), 0)
            zheng[(i + j, a[i][j])] = getz((i + j, a[i][j]), 0) + 1
            ans += getf((i - j, a[i][j]), 0)
            fan[(i - j, a[i][j])] = getf((i - j, a[i][j]), 0) + 1
    print(ans * 2)
if __name__ == "__main__":
    main()
