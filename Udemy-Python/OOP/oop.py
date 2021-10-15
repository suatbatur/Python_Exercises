# class Araba():
#     model= "megane"
#     renk = "gümüs"
#     beygir_gücü = 110
#     silindir = 4
    
# araba1 = Araba()
# araba2 = Araba()
# print(araba1)
# print(araba2)


# print(araba1.model)
# print(araba2.beygir_gücü)
# class Araba():
    
#     def __init__(self,model,renk,beygir_gücü,silindir):
        
#         self.model = model
#         self.renk =renk
#         self.beygir_gücü = beygir_gücü
#         self.silindir = silindir
        
# araba1=Araba("megane","gümüs",110,4)
# araba2=Araba("a3","siyah",150,6)

# print(araba1.model)
# print(araba2.model)


#---------------------metodlar--------------------------

# class Yazılımcı():
    
#     def __init__(self,isim,soyisim,numara,maas,diller):
#         self.isim =isim
#         self.soyisim =soyisim
#         self.numara =numara
#         self.maas =maas
#         self.diller = diller
    
#     def bilgilerigöster(self):
#         print("""
#               Yazılımcı objesinin özellikleri :
              
#               İsim : {}
#               Soyisim : {}
#               Numara : {}
#               Maas : {}
#               Bildiği diller : {}
#               """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))   
      
#     def zam_yap(self,zam_miktarı):
#         print("zam yapılıyor")
#         self.maas +=zam_miktarı
        
#     def dil_ekle(self,yeni_dil):
#         print("dil ekleniyor")
#         self.diller.append(yeni_dil)
                
        
            
# yazılımcı1 = Yazılımcı("suat","batur",2455,4000,["python","JS"])   
# yazılımcı1.bilgilerigöster()
# yazılımcı1.dil_ekle("java")
# yazılımcı1.zam_yap(250)
# yazılımcı1.bilgilerigöster()

