n = 0
for i in range(12345678,98765433):
    s=str(i)
    a = s.find('2')
    if a == -1:
        continue
    b = s.find('0',a)
    if b == -1:
        continue
    c = s.find('2',b)
    if c == -1:
        continue
    d = s.find('3',c)
    if d == -1:
        continue
    n += 1
print(98765433-12345678-n)
#找包含的