import sys
n = int(input())
l = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
def rotate_matrix(n, mat):
    res = [[0] * n for _ in range(n)]
    #核心思想：大矩阵坐标换成小矩阵
    for i in range(n):
        for j in range(n):
            k = min(i, j, n-1-i, n-1-j)  #判断层数，距离四条边最短
            #小的边长
            s = n - 2 * k
            x = i - k
            y = j - k
            if k % 2 == 0:
                # 顺时针 90°
                nx, ny = y, s - 1 - x
            else:
                # 逆时针 90°
                nx, ny = s - 1 - y, x
            #回到全局坐标
            ni = k + nx
            nj = k + ny
            res[ni][nj] = mat[i][j]
    return res

res = rotate_matrix(n, l)
for row in res:
    print(' '.join(map(str, row)))