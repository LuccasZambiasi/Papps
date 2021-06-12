# Funcao de Boas-Vindas
def inicio():
    print('''
Bem-vindo a calculadora!
''')
...

# Funcao de Calculo
def calculo():
    operation = input('''
Escolha a operacao matematica que deseja fazer:
+ para adicao
- para subtracao
* para multiplicacao
/ para divisao
% para o modulo

''')

    # Entrada
    number_1 = int(input('Digite o primeiro numero: '))
    number_2 = int(input('Digite o segundo numero: '))

    # Calculo da Adicao
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # Calculo da Subtracao
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    # Calculo da Multiplicao
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Calculo da Divisao
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    # Calculo do Modulo
    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 / number_2)    

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
