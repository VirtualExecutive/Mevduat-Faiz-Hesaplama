

class Zaman:
    zamanStr : str
    istenilenZaman : int
    gecenZaman = 1

    def GecenZamaniArtir() -> None:
        Zaman.gecenZaman +=1

    def ZamanDoldumu() -> bool:
        return not Zaman.gecenZaman <= Zaman.istenilenZaman