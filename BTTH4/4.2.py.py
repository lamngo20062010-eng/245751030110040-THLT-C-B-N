print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("3)")
class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
    
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
