print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("21)")
print("Vui lòng nhập chuỗi các số nhị phân gồm 4 số (phân tách bởi dấu phẩy):")
binary_input = input()
numbers = binary_input.split(',')
divisible_by_5 = []
for num_str in numbers:
    num_str = num_str.strip()
    try:
        decimal_num = int(num_str, 2)
        if decimal_num % 5 == 0:
            divisible_by_5.append(num_str)      
    except ValueError:
        pass
print(",".join(divisible_by_5))
