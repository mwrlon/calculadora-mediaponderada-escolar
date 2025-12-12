## Calculadora de Média Ponderada

import time

## Calcular os pesos dos trimestres 
print('Olá usuário, seja bem vindo a calculadora automática de média ponderada!')
time.sleep(3)
print('Vale ressaltar que essa calculadora ainda está em construção e no maximo, a soma dos pesos devem ser 10!')
time.sleep(3)
print('Isso também vale para os valores, que cada um deles nao devem passar de 10!')
time.sleep(3)
print('Vamos começar escolhendo se você deseja calcular a média com 2, 3 ou 4 pesos no total!')
time.sleep(3)
print('Digite "2" para 2 Pesos')
print('Digite "3" para 3 Pesos')
print('Digite "4" para 4 Pesos')
escolha = int(input(''))

if (escolha == 2):
    peso1 = int(input('Qual é o valor do primeiro peso? '))
    time.sleep(0.5)
    peso2 = int(input('Qual é o valor do segundo peso? '))
    time.sleep(0.5)

    while (peso1 + peso2 > 10):
        print('A soma dos pesos foi maior que 10! Por favor, digite os pesos novamente.')
        break

    nota1 = float(input('Digite seu primeiro valor: '))
    time.sleep(0.5)
    nota2 = float(input('Digite seu segundo valor: '))
    time.sleep(0.5)

    while (nota1 > 10 or nota2 > 10):
        print('Alguma das notas que você inseriu passou de 10! Por favor, digite suas notas novamente.')
        break

    media = ((nota1 * peso1) + (nota2 * peso2))/10

    print(f'Sua média obtida no final foi de: {media}!')

elif (escolha == 3):
    peso1 = int(input('Qual é o valor do primeiro peso? '))
    time.sleep(0.5)
    peso2 = int(input('Qual é o valor do segundo peso? '))
    time.sleep(0.5)
    peso3 = int(input('Qual é o valor do terceiro peso? '))
    time.sleep(0.5)
    nota1 = float(input('Digite seu primeiro valor: '))
    time.sleep(0.5)
    nota2 = float(input('Digite seu segundo valor: '))
    time.sleep(0.5)
    nota3 = float(input('Digite seu terceiro valor: '))
    time.sleep(0.5)
    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / 10

    while (peso1 + peso2 + peso3 > 10):
        print('A soma dos pesos foi maior que 10! Por favor, digite os pesos novamente.')
        break
    while (nota1 > 10 or nota2 > 10 or nota3 > 10):
        print('Alguma das notas que você inseriu passou de 10! Por favor, digite suas notas novamente.')
        break
    print(f'Sua média obtida no final foi de: {media}!')

elif (escolha == 4):
    peso1 = int(input('Qual é o valor do primeiro peso? '))
    time.sleep(0.5)
    peso2 = int(input('Qual é o valor do segundo peso? '))
    time.sleep(0.5)
    peso3 = int(input('Qual é o valor do terceiro peso? '))
    time.sleep(0.5)
    peso4 = int(input('Qual é o valor do quarto peso? '))
    time.sleep(0.5)
    nota1 = float(input('Digite seu primeiro valor: '))
    time.sleep(0.5)
    nota2 = float(input('Digite seu segundo valor: '))
    time.sleep(0.5)
    nota3 = float(input('Digite seu terceiro valor: '))
    time.sleep(0.5)
    nota4 = float(input('Digite seu quarto valor: '))
    time.sleep(0.5)
    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3) + (nota4 * peso4)) / 10

    while (peso1 + peso2 + peso3 + peso4 > 10):
        print('A soma dos pesos foi maior que 10! Por favor, digite os pesos novamente.')
        break
    while (nota1 > 10 or nota2 > 10 or nota3 > 10 or nota4 > 10):
        print('Alguma das notas que você inseriu passou de 10! Por favor, digite suas notas novamente.')
        break
    print(f'Sua média obtida no final foi de: {media}!')

else:
    print('Por favor, escolha um dos pesos selecionados! ')