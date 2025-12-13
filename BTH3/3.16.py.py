print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("17)")
def tinh(so):
    tong = 0
    for i in range(1, so // 2 + 1):
        if so % i == 0:
            tong += i
    return tong
n = int(input("Nhập số nguyên dương n: "))
print(f"Các số nguyên dương nhỏ hơn {n} có tổng ước lớn hơn chính nó là:")
for i in range(1, n):
    if tinh(i) > i:
        print(i)
