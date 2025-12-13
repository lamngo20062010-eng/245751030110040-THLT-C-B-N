print("Ngô Xuân Lâm")
print("MSV: 245751030110040")
print("9)")
str=input("Nhập xâu kí tự:")
dict={}
for n in str:
   keys=dict.keys()
   if n in keys:
        dict[n]+=1
   else:
        dict[n]=1
print(dict)
