# Funcao de Boas-Vindas
def inicio():
    print('''
Bem-vindo ao Conversor!
''')
...

# Funcao de Calculo
def calculo():
    operation = input('''
Escolha a operacao que deseja fazer:
A - Graus pra Fahrenheit
B - Graus para Kelvin
C - Fahrenheit para Graus
D - Fahrenheit para Kelvin
E - Kelvin para Graus
F - Kelvin para Fahrenheit

''')

    # Entrada
    temp = int(input('Digite a temperatura: '))

    # C > F
    if operation == 'A':
        x = 1.8*temp + 32
        print(temp, ' Graus em Fahrenheit: ', x)

    # C > K
    if operation == 'B':
        x = temp + 273.15
        print(temp, ' Graus em Kelvin: ', x)

    # F > C 
    if operation == 'C':
        x = (temp - 32) * 5/9
        print(temp, ' Fahrenheit em Graus: ', round(x, 2))
    
    # F > K 
    if operation == 'D':
        x = (temp - 32) * 5/9 + 273.15
        print(temp, ' Fahrenheit em Kelvin: ', round(x, 2))

    # F > K 
    if operation == 'E':
        x = temp - 273.15
        print(temp, ' Kelvin em Graus: ', x)

    # F > K 
    elif operation == 'F':
        x = (temp - 273.15) * 9/5 + 32
        print(temp, ' Kelvin em Fahrenheit: ', round(x, 2))

    # Operacao Invalida
    else:
        print('Voce digitou uma operacao invalida. Tente novamente.')

    repeticao()

# Funcao de Repeticao
def repeticao():

    # Entrada
    calc_novamente = input('''
Voce quer calcular novamente?
Digite S pra SIM e N para NAO.
''')

    # Verificacao
    if calc_novamente.upper() == 'S':
        calculo()
    elif calc_novamente.upper() == 'N':
        print('Tenha um bom dia/noite.')
    else:
        repeticao()

# Inicio do Programa
inicio()
calculo()
