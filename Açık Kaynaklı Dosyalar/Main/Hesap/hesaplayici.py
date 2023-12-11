from .Hesaplayici.zaman import *

class Hesaplayici:
    aylikHesapmi : bool
    zamanFormulu : float

    def KarHesapla(miktar, faiz) -> float:
        return  float((miktar*faiz) / (Hesaplayici.zamanFormulu))

    def HesaplamaYontemiAyarla(aylikmi) -> None:
        if(aylikmi):
            Hesaplayici.zamanFormulu = 36500/12
            Zaman.zamanStr = "Ay"
        else:
            Hesaplayici.zamanFormulu = 36500
            Zaman.zamanStr = "Gün"

