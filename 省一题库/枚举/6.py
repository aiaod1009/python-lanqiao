ans = 0
for r in range(0,256):
    for g in range(0, 256):
        for b in range(0, 256):
            if b > g and b > r:
                ans+=1
print(ans)