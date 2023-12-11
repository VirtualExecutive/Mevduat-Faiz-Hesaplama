
class Giris():
    def MiktarSor() -> float:
        while(True):
            girdi = input("Başlangıç miktarı ne kadar?: ")
            try:
                girdi = float(girdi)
                return girdi
            except:
                print("Hatalı değer girdiniz! Tam sayı girmelisiniz.\n")

    def FaizSor() -> float:
        while(True):
            girdi = input("Faiz yüzde kaç girilecek?: ").replace(",",".").replace("%","")
            try:
                girdi = float(girdi)
                return girdi
            except ValueError:
                print("Hatalı değer girdiniz!\nÖrnek: 45.5% | 45% | 45.0\n")
            

    def HesaplamaYontemiSor() -> bool:
        while(True):
            girdi = input("Vadeniz aylık olarak mı hesaplanacak? \n (E)vet | (H)ayır : ").lower()
            if(girdi=="e"):
                return True
            elif(girdi=="h"):
                return False
            else:
                print("\nCevabınız (E)vet ise E yazınız, (H)ayır ise H yazınız. \n")
    
    def VadeSuresiSor() -> int :
        while(True):
            girdi = input("Kaç gün&ay boyunca tekrarlanacak: ")
            try:
                girdi = int(girdi)
                return girdi
            except ValueError:
                print("Hatalı değer girdiniz! Tam sayı girmelisiniz.\n")