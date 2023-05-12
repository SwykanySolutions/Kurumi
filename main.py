from config import *
from tools.falar_texto import *
from tools.ouvir_audio import *
from utilities.temperatura.temperatura import *


def main():
    while True:
        start = ouvir()
        if "kurumi" in start:
            falar("olá eu sou a Kurumi")
            comando = start.split('kurumi ')[1]
            if "qual a temperatura em " in comando:
                comando_temp = comando.split('qual a temperatura em ')[1]
                resposta = clima('temperatura', comando_temp)
                falar(resposta)
            
            elif "desativar" in comando:
                falar("desligando........")
                break
        

if __name__ == "__main__":
    main()
