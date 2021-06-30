from datetime import datetime, date
print("doğum tarihinizi giriniz")
gun=int(input("gün degeri: "))
ay=int(input( "ay degeri: "))
yıl=int(input("yıl degeri: "))

b_date = date(year = yıl, month = ay, day = gun)

if (b_date.month==12 and 22<=b_date.day<=31) or (b_date.month==1 and 1<=b_date.day<=21):
    print("oğlak")
elif (b_date.month==1 and 22<=b_date.day<=31) or (b_date.month==2 and 1<=b_date.day<=19):
    print("kova")
elif (b_date.month==2 and 20<=b_date.day<=29) or (b_date.month==3 and 1<=b_date.day<=20):
    print("balık")
elif (b_date.month==3 and 21<=b_date.day<=31) or (b_date.month==4 and 1<=b_date.day<=20):
    print("koç")
elif (b_date.month==4 and 21<=b_date.day<=30) or (b_date.month==5 and 1<=b_date.day<=21):
    print("boğa")
elif (b_date.month==5 and 22<=b_date.day<=31) or (b_date.month==6 and 1<=b_date.day<=22):
    print("ikizler")
elif (b_date.month==6 and 23<=b_date.day<=30) or (b_date.month==7 and 1<=b_date.day<=22):
    print("yengeç")
elif (b_date.month==7 and 23<=b_date.day<=31) or (b_date.month==8 and 1<=b_date.day<=22):
    print("aslan")
elif (b_date.month==8 and 23<=b_date.day<=31) or (b_date.month==9 and 1<=b_date.day<=22):
    print("başak")
elif (b_date.month==9 and 23<=b_date.day<=30) or (b_date.month==10 and 1<=b_date.day<=22):
    print("terazi")
elif (b_date.month==10 and 23<=b_date.day<=31) or (b_date.month==11 and 1<=b_date.day<=21):
    print("akrep")
elif (b_date.month==11 and 22<=b_date.day<=30) or (b_date.month==12 and 1<=b_date.day<=21):
    print("yay")






