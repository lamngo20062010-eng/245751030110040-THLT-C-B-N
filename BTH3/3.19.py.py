print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("20)")
import math
def pascal_triangle(n_rows):
      for i in range(n_rows):
        row_values = []
        for j in range(i + 1):
            coeff = 1
            if j > i - j:
                j = i - j
            for k in range(j):
                coeff = coeff * (i - k) // (k + 1)
            row_values.append(str(coeff))     
        print(" ".join(row_values))
try:
    n_input = int(input("Nhập số dòng n: "))
    if n_input <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        print(f"--- Tam giác Pascal với {n_input} dòng ---")
        pascal_triangle(n_input)
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
