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

#============= INSERIR TRANSPORTE NA LISTA ==================
    transporte = []

    bic = input('Você utiliza bicicleta como meio de transporte? (S/N): ').upper()
    while bic not in ['S', 'N']:
        print('Opção inválida!')
        bic = input('Você utiliza bicicleta como meio de transporte? (S/N): ').upper()
    if bic == 'S':
        transporte.append('bicicleta')
    
    pub = input('Você utiliza transporte público? (S/N): ').upper()
    while pub not in ['S', 'N']:
        print('Opção inválida!')
        pub = input('Você utiliza transporte público? (S/N): ').upper()
    if pub == 'S':
        transporte.append('transporte público')

    caminhada = input('Você costuma fazer caminhada para ir aos lugares? `(S/N):').upper()
    while caminhada not in ['S', 'N']:
        print('Opcão inválida!')
        caminhada = input('Você costuma fazer caminhada para ir aos lugares? `(S/N):').upper()
    if caminhada == 'S':
        transporte.append('caminhada')

    carroC = input('Você utiliza carro com commbustivel fossil para se locomover? (S/N): ').upper()
    while carroC not in ['S', 'N']:
        print('Opção inválida!')
        carroC = input('Você utiliza carro com commbustivel fossil para se locomover? (S/N): ').upper()
    if carroC == 'S':
        transporte.append('carroC')
    



    restart = input('Quer fazer uma outra analise? (S/N): ').upper()
    while restart not in ['S', 'N']:
        print('Opção inválida!')
        restart = input('Quer fazer uma outra analise? (S/N): ').upper()
