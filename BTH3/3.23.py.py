print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("24)")
print("Vui lòng nhập một câu:")
input_string = input()
upper_count = 0
lower_count = 0
for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print(f"Chữ hoa: {upper_count}")
print(f"Chữ thường: {lower_count}")

