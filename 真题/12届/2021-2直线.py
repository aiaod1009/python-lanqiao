import math
from fractions import Fraction

points = [(x,y) for x in range(20) for y in range(21)]
lines = set()

for i in range(len(points)):
  x1,y1 = points[i]
  for j in range(i + 1,len(points)):
    x2,y2 = points[j]
    if x1 == x2:
      lines.add(('x',x1))
    else:
      k = Fraction(y2 - y1,x2 - x1)
      b = y1 - k * x1
      lines.add((k,b))

print(len(lines))