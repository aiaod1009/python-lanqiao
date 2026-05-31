ans = 0
for d in range(1,(2025-1)//2+1):
    for i in range(1,2026):
        if i + 2*d <= 2025:
            ans += 1
print(2*ans)