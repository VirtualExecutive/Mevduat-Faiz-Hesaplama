from Main.giris import *
from Main.hesap import *
from Main.cikti import *



class Main:
    def Start():
        Hesap.miktar = Hesap.ilkMiktar = Giris.MiktarSor()
        Zaman.istenilenZaman = Giris.VadeSuresiSor()
        Hesaplayici.aylikHesapmi = Giris.HesaplamaYontemiSor()
        Hesap.faiz = Giris.FaizSor()

        Hesaplayici.HesaplamaYontemiAyarla(Hesaplayici.aylikHesapmi)

        while(not Zaman.ZamanDoldumu()):
            kar = Hesaplayici.KarHesapla(Hesap.miktar,Hesap.faiz)
            Cikti.AnlikIstatistikYazdir(Zaman.zamanStr, Zaman.gecenZaman, Hesap.miktar, kar)
            Hesap.ParaEkle(kar)
            Zaman.GecenZamaniArtir()
            


    


if __name__ == "__main__":
    Main.Start()