
import mateus
import eric

op = int(input('Digite a operação que deseja:\n1 - Soma / 2 - Subtração / 3 - Multiplicação / 4 - Divisão\n'))
v1 = int(input('Digite o valor 1:\n'))
v2 = int(input('Digite o valor 2:\n'))

if op == 1:
    print(eric.soma(v1,v2))

if op == 2:
    print(mateus.menos(v1,v2))

if op == 3:
    print(eric.vezes(v1,v2))

if op == 4:
    print(mateus.divisao(v1,v2))
