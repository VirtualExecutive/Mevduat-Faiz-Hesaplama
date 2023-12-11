from .Hesap.hesaplayici import *

class Hesap:
    faiz : float
    miktar : float
    ilkMiktar : float

    def ParaEkle(miktar) -> None:
        Hesap.miktar += miktar
