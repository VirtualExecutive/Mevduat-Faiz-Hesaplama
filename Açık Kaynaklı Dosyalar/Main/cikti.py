

class Cikti():
    zamanStr:str

    def AnlikIstatistikYazdir(zamanStr:str, gecenZaman:int, miktar:float,kar:float) -> None:
        print(f"{gecenZaman}. {zamanStr} | {miktar} + {kar} = {miktar+kar}")