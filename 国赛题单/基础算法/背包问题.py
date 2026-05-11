import sys
input = lambda:sys.stdin.readline().strip()
T = int(input())
for _ in range(T):
    b1,b2,b3 = map(int,input().split())
    a,b = map(int,input().split())
    va,vb = map(int,input().split())
    ans = 0
    if va < vb:
        a, b = b, a
        va, vb = vb, va
    for a1 in range(min(a, b1 // va) + 1):
        can_b1 = (b1 - a1 * va) // vb
        rem_a1 = a - a1
        for a2 in range(min(rem_a1, b2 // va) + 1):
            can_b2 = (b2 - a2 * va) // vb
            rem_a2 = rem_a1 - a2
            for a3 in range(min(rem_a2, b3 // va) + 1):
                can_b3 = (b3 - a3 * va) // vb
                total_A = a1 + a2 + a3
                total_B = min(b, can_b1 + can_b2 + can_b3)
                if total_A + total_B > ans:
                    ans = total_A + total_B
    print(ans)