print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("6)")
class IOString:
    def __init__(self):      
        self.str1 = "" 
    def get_String(self):
        self.str1 = input("Nhập chuỗi của bạn: ")
    def print_String(self):
        print(self.str1.upper())
if __name__ == "__main__":
    str1_instance = IOString()
    str1_instance.get_String()
    str1_instance.print_String()
