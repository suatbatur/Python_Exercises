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
class Araba():
    
    def __init__(self,model,renk,beygir_gücü,silindir):
        
        self.model = model
        self.renk =renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir
        
araba1=Araba("megane","gümüs",110,4)
araba2=Araba("a3","siyah",150,6)

print(araba1.model)
print(araba2.model)



