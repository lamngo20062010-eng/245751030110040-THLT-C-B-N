print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("18)")
n = int(input("Nhập số nguyên dương n: "))
alist = []
a,b = 0,1
while a < n:
    alist.append(a)
    a,b = b,a + b
print(f"Dãy Fibonacci nhỏ hơn {n}: {alist}")
