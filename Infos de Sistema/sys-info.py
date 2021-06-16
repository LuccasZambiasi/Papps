import os
import time
import platform

def main():
    os.system("clear")
    print("")
    print("\033[91m\tTempo e Hora: \033[0m" + time.ctime())
    print("\033[91m\tDiretorio atual: \033[0m" + os.getcwd())
    print("\033[91m\tSistema Operacional: \033[0m" + platform.system())
    print("\033[91m\tNome: \033[0m" + platform.node())
    print("\033[91m\tVersao do OS: \033[0m" + platform.uname()[3])
    print("\033[91m\tEstrutura: \033[0m" + platform.architecture()[0])
    print("")

if __name__ == "__main__":
    main()
