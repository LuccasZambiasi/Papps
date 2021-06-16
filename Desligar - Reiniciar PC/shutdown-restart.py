import os

print(
    "Esse programa e usado para desligar/reiniciar um computador. Escolha sua opcao: "
)
print("1. Desligar imediatamente")
print("2. Desligar apos determinado tempo")
print("3. Reiniciar imediatamente")
print("4. Reiniciar apos determinado tempo")
print("5. Sair")
print(end="Digite sua escolha: ")

choice = int(input())

if choice == 1:
    os.system("shutdown /s /t 0")

elif choice == 2:
    print(end="Digite o valor em segundos: ")
    sec = int(input())
    strOne = "shutdown /s /t "
    strTwo = str(sec)
    str = strOne + strTwo
    os.system(str)

elif choice == 3:
    os.system("shutdown /r /t 0")

elif choice == 4:
    print(end="Digite o valor em segundos: ")
    sec = int(input())
    strOne = "shutdown /r /t "
    strTwo = str(sec)
    str = strOne + strTwo
    os.system(str)

elif choice == 5:
    exit()
else:
    print("Escolha errada!")
