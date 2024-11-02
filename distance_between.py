import math
x1=int(input("co-ordinate "))
x2=int(input("co-ordinate "))
y1=int(input("co-ordinate "))
y2=int(input("co-ordinate "))

distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("distance between the points =",distance)