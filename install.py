from time import sleep
import subprocess
import os

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

print("Iniciando o processo de instalação em 3 segundos.")
sleep(3)
subprocess.check_call(["pip", "install", "colorama"])
clear_console()
from colorama import init, Fore, Back, Style
print(Fore.LIGHTGREEN_EX+"Instalação concluída, aguarde 3 segundos.",Fore.WHITE+"")
sleep(3)
clear_console()
exit()
