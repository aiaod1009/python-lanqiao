s = ''
for i in range(1,2024):
    s += str(i)
t = '2023'
dp = [0] * 4
for c in s:
    if c == t[3]:
        dp[3] += dp[2]
    if c == t[2]:  # '2'
        dp[2] += dp[1]
    if c == t[1]:  # '0'
        dp[1] += dp[0]
    if c == t[0]:  # '2'
        dp[0] += 1
print(dp[3])
#不用拼接也可以,直接range(1,2024)

# if(s[i] == '2'){
#     dp[0]++;
#     dp[2] += dp[1];
# }
# else if(s[i] == '0'){
#     dp[1] += dp[0];
# }
# else if(s[i] == '3'){
#     dp[3] += dp[2];
# }