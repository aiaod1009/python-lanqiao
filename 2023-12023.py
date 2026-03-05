def solve(digit):
    digit = str(digit)
    count = 0
    for j in digit:
        if j == "2" and count == 0:
            count = 1
        elif j == "0" and count == 1:
            count = 2
        elif j == "2" and count == 2:
            count = 3
        elif j == "3" and count == 3:
            count = 4
    if count == 4:
        return True


ans = 0
for i in range(12345678, 98765433):
    if solve(i):
        ans += 1
print(98765432 - 12345678 - ans)