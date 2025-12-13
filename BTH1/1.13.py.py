print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("13)")
import math
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
d=b*b-4*a*c
if d<0:
   print("Phương trình vô nghiệm")
elif d==0:
   x=(-b)/(2*a)
   print("Phương trình có nghiệm kép là:",x)
elif d>0:
   y=(-b-math.sqrt(d))/(2*a)
   z=(-b+math.sqrt(d))/(2*a)
   print("Phương trình có nghiệm x1 là:",y)
   print("Phương trình có nghiệm x2 là:",z)


