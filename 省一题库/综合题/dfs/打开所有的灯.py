from collections import deque
flip = [
    [0, 1, 3], [0, 1, 2, 4], [1, 2, 5],
    [0, 3, 4, 6], [1, 3, 4, 5, 7], [2, 4, 5, 8],
    [3, 6, 7], [4, 6, 7, 8], [5, 7, 8]
]
def min_steps(ini):
    target = "111111111"
    if ini == target:
        return 0
    visited = set()   # 记录已经访问过的状态，避免重复搜索
    q = deque([(ini, 0)])  # 队列存 (当前状态, 当前步数)
    visited.add(ini)    # 初始状态标记为已访问
    while q:  # 队列不为空就继续搜
        s, step = q.popleft()    # 取出队首元素（最早加入的，步数最少）
        for i in range(9):
            lst = list(s)
            for j in flip[i]:
                lst[j] = '1' if lst[j] == '0' else '0'
            new_s = ''.join(lst)
            if new_s == target:
                return step + 1
            if new_s not in visited:
                visited.add(new_s)
                q.append((new_s, step + 1))
    return -1
s = ""
for _ in range(3):
    row = input().split()
    s += ''.join(row)
print(min_steps(s))