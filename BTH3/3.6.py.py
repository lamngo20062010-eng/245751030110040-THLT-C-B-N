print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("7)")
chuoigoc = input("Nhập một chuỗi (bao gồm chữ và số): ")
chuoimoi = ""
for kitu in chuoigoc:
    if not kitu.isdigit():
        chuoimoi += kitu
print(f"Chuỗi mới sau khi loại bỏ chữ số: {chuoimoi}")
