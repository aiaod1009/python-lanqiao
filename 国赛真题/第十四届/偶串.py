n = input()
n_ = set(n)
for i in n_:
  if n.count(i)%2==0:
    result = "YES"
    continue
  else:
    result = "NO"
    break
print(result)