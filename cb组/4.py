T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    max_a = max(A)
    if total % 5 == 0 and max_a <= total // 5:
        print("T")
    else:
        print("F")