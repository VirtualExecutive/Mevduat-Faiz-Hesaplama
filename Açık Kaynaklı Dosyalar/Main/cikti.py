

class Cikti():
    zamanStr:str

    def AnlikIstatistikYazdir(zamanStr:str, gecenZaman:int, miktar:float,kar:float) -> None:
        print(f"{gecenZaman}. {zamanStr} | {(miktar):0.2f} + {(kar):0.2f} = {(miktar+kar):0.2f}")