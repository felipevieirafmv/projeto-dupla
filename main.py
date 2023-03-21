
import mateus
import eric

while True:
    while True:
        try:
            op = int(input('Digite a operação que deseja:\n1 - Soma / 2 - Subtração / 3 - Multiplicação / 4 - Divisão\n'))

            break
        except ValueError:
            print("Digite um número válido!\n")

    while True:
        try:
            v1 = int(input('Digite o valor 1:\n'))
            break
        except ValueError:
            print("Digite um número válido!\n")

    while True:
        try:
            v2 = int(input('Digite o valor 2:\n'))
            break
        except ValueError:
            print("Digite um número válido!\n")

    print('')

    if op == 1:
        print(eric.soma(v1,v2))

    if op == 2:
        print(mateus.menos(v1,v2))

    if op == 3:
        print(eric.vezes(v1,v2))

    if (op == 4) and (v2!=0):
        print(mateus.divisao(v1,v2))
    elif op == 4 and v2 == 0:
        print("Impossível dividir por zero")

    parar = input('\nDigite 0 se deseja parar, ou qualquer outro valor para continuar:\n')
    if parar =='0':
        break
