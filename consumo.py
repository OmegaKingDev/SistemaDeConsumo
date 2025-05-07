from datetime import date
restart = 'S'


agua = 0

while restart == 'S':
    data = date.today()

    agua = float(input('Digite o consumo de água em litros: '))
    while agua <= 0:
        print('Valor inválido!')
        agua = float(input('Digite o consumo de água em litros: '))

    reciclavel = float(input('Informe a quantidade de lixo reciclável em kg: '))
    while reciclavel <= 0:
        print('Valor inválido!')
        reciclavel = float(input('Informe a quantidade de lixo reciclável em kg: '))

    lixo = float(input('Informe a quantidade de lixo total produzido: '))
    while lixo <= 0:
        print('Valor inválido!')
        lixo = float(input('Informe a quantidade de lixo total produzido: '))

    energia = float(input('Digite o consumo de energia em kWh: '))
    while energia <= 0:
        print('Valor inválido!')
        energia = float(input('Digite o consumo de energia em kWh: '))

    bic = input('Você utiliza bicicleta como meio de transporte? (S/N): ').upper()
    while bic not in ['S', 'N']:
        print('Opção inválida!')
        bic = input('Você utiliza bicicleta como meio de transporte? (S/N): ').upper()


    restart = input('Quer fazer uma outra analise? (S/N): ').upper()
    while restart not in ['S', 'N']:
        print('Opção inválida!')
        restart = input('Quer fazer uma outra analise? (S/N): ').upper()
    