scores = set()

# 枚举每一类题目的数量
for a in range(3):  # 5分题：0,1,2道 → 0,5,10分
    for b in range(3):  # 10分题：0,1,2道 → 0,10,20分
        for c in range(3):  # 15分题：0,1,2道 → 0,15,30分
            for d in range(3):  # 20分题：0,1,2道 → 0,20,40分
                for e in range(3):  # 25分题：0,1,2道 → 0,25,50分
                    total = a*5 + b*10 + c*15 + d*20 + e*25
                    scores.add(total)

print(len(scores))