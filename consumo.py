from datetime import date
restart = 'S'

while restart == 'S':
    data = date.today()

#================= CONSUMO ==================================
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

#================= CONSUMO ANALISE =============================
    if agua < 150:
        aguaS = 'Alta sustentabilidade de água'

    elif agua <= 200:
        aguaS = 'Sustentabilidade moderada de água'

    else:
        aguaS = 'Baixa sustentabilidade de água'

#============= INSERIR TRANSPORTE NA LISTA ======================

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
        transporte.append('transporteP')

    caminhada = input('Você costuma fazer caminhada para ir aos lugares? (S/N):').upper()
    while caminhada not in ['S', 'N']:
        print('Opcão inválida!')
        caminhada = input('Você costuma fazer caminhada para ir aos lugares? (S/N):').upper()
    if caminhada == 'S':
        transporte.append('caminhada')

    carroC = input('Você utiliza carro com combustivel fossil para se locomover? (S/N): ').upper()
    while carroC not in ['S', 'N']:
        print('Opção inválida!')
        carroC = input('Você utiliza carro com combustivel fossil para se locomover? (S/N): ').upper()
    if carroC == 'S':
        transporte.append('carroC')
    
    carroE = input('Você utiliza carro elétrico como meio de transporte? (S/N): ').upper()
    while carroE not in ['S', 'N']:
        print('Opção inválida!')
        carroE = input('Você utiliza carro elétrico como meio de transporte? (S/N): ').upper()
    if carroE == 'S':
        transporte.append('carroE')

    carona = input('Você costuma usar de carona como meio de transporte? (S/N): ').upper()
    while carona not in ['S','N']:
        print('Opção inválida!')
        carona = input('Você costuma usar de carona como meio de transporte? (S/N): ').upper()
    if carona == 'S':
        transporte.append('carona')

#================== analise transporte ======================

    alta = ['caminhada', 'carroE', 'bicicleta', 'transporteP']
    moderado = ['carroC', 'carona']

    if any(v in transporte for v in alta):
        sustentabilidade = 'Alta sustentabilidade'

    elif any(v in transporte for v in moderado):
        sustentabilidade = 'Sustentabilidade moderada'

    else:
        sustentabilidade = 'Baixa sustentabilidade'

    if not any(v in transporte for v in alta):
        sustentabilidade = 'Baixa sustentabilidade'

#============== PRINT DAS ANALISES ===================


    print(sustentabilidade)

#==================== RESTART ========================

    restart = input('Quer fazer uma outra analise? (S/N): ').upper()
    while restart not in ['S', 'N']:
        print('Opção inválida!')
        restart = input('Quer fazer uma outra analise? (S/N): ').upper()
