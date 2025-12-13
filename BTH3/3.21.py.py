print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("22)")
def check_even_digits(number):
    s_num = str(number)
    for digit_char in s_num:
        digit = int(digit_char)
        if digit % 2 != 0:
            return False
    return True
even_digit_numbers = []
for i in range(1000, 3001):
    if check_even_digits(i):
        even_digit_numbers.append(str(i))
print(",".join(even_digit_numbers))
