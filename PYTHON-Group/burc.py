from datetime import datetime, date
print("doğum tarihinizi giriniz")
gun=int(input("gün degeri: "))
ay=int(input( "ay degeri: "))
yıl=int(input("yıl degeri: "))

b_date = date(year = yıl, month = ay, day = gun)

if (b_date.month==12 and 22<=b_date.day<=31) or (b_date.month==1 and 1<=b_date.day<=21):
    print("oğlak") 








