#只能过60%
# n = int(input())
# tot = 0
# while n > 0:
#     n -= sum(int(i) for i in str(n))
#     tot += 1
# print(tot)

#过100%
s = int(input())
answer = 0
while s != 0:
    answer += 1
    remove = 0
    #反转，用str那些转化的话效率很慢
    n = s
    while n != 0:
        remove += n % 10
        n //= 10
    s -= remove
print(answer)
