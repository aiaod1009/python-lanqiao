# n,k = map(int,input().split())
# path = []
# def dfs():
#     if len(path) == n:
#         print(' '.join(map(str,path)))
#         return
#     for i in range(1,k+1):
#         path.append(i)
#         dfs()
#         path.pop()
# dfs()

n, k = map(int, input().split())
res = [0] * n
def dfs(pos):
    if pos == n:
        print(''.join(map(str,res)))
        return
    for i in range(1,n+1):
        res[pos] = i
        dfs(pos+1)
dfs(0)


# n = 2
# k = 3
# path = []
# # 记录递归层级，方便看执行顺序
# level = 0
#
#
# def dfs():
#     global level
#     level += 1  # 进入递归，层级+1
#     current_level = level  # 保存当前层级
#
#     # 打印当前状态
#     print(f"【层级{current_level}】进入dfs，path={path}")
#
#     # 终止条件：path长度等于n
#     if len(path) == n:
#         print(f"【层级{current_level}】满足条件，输出: {' '.join(map(str, path))}")
#         level -= 1  # 退出递归，层级-1
#         return
#
#     # 遍历1~k
#     for i in range(1, k + 1):
#         print(f"【层级{current_level}】for循环 i={i}，准备append")
#         path.append(i)
#         print(f"【层级{current_level}】append后 path={path}")
#
#         # 递归调用下一层
#         dfs()
#
#         # 递归返回后，执行pop
#         print(f"【层级{current_level}】递归返回，准备pop")
#         path.pop()
#         print(f"【层级{current_level}】pop后 path={path}")
#
#     level -= 1  # 退出递归，层级-1
#     print(f"【层级{current_level}】for循环结束，退出dfs")
#
#
# # 启动DFS
# dfs()