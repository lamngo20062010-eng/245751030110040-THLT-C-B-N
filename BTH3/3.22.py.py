print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("23)")
print("Vui lòng nhập một câu:")
input_string = input()
letters_count = 0
digits_count = 0
for char in input_string:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
print(f"Số chữ cái là: {letters_count}")
print(f"Số chữ số là: {digits_count}")
