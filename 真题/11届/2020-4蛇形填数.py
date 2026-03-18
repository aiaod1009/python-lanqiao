i_target = 20
j_target = 20

# 1. 计算所在斜行k
k = i_target + j_target - 1  # 39

# 2. 计算前k-1斜行的总数字数（1+2+...+38）
sum_before = (k - 1) * k // 2  # 38×39//2=741

# 3. 计算目标数（奇数斜行，偏移量=k - i_target）
result = sum_before + (k - i_target + 1)  # 741 + (39-20+1)=761

print(result)  # 直接输出761
