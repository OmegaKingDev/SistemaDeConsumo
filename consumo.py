from datetime import date
restart = 'S'
agua = 0
reciclavel = 0
lixo = 0
energia = 0

aguaS = 0
reciclavelS = 0
energiaS = 0



#================= FUNÇÕES ==================================
def error():
    print('Valor inválido!')

#======================================================== ====   


#================= CONSUMO ==================================

def consumo():
    agua = float(input('Digite o consumo de água em litros: '))
    while agua <= 0:
        error()
        agua = float(input('Digite o consumo de água em litros: '))

    reciclavel = float(input('Informe a porcentagem de lixo reciclado: '))
    while reciclavel <= 0:
        error()
        reciclavel = float(input('Informe a quantidade de lixo reciclável em kg: '))

    lixo = float(input('Informe a quantidade de lixo total produzido: '))
    while lixo <= 0:
        error()
        lixo = float(input('Informe a quantidade de lixo total produzido: '))

    energia = float(input('Digite o consumo de energia em kWh: '))
    while energia <= 0:
        error()
        energia = float(input('Digite o consumo de energia em kWh: '))

#================= CONSUMO ANALISE =============================
    if agua < 150:
        aguaS = 'Alta sustentabilidade de água'

    elif agua <= 200:
        aguaS = 'Sustentabilidade moderada de água'

    else:
        aguaS = 'Baixa sustentabilidade de água'

    if reciclavel > 50:
        reciclavelS = 'Alta sustentabilidade de reciclagem de lixo'

    elif reciclavel > 20:
        reciclavelS = 'Sustentabilidade moderada de reciclagem de lixo'
        
    else:
        reciclavelS =  'Baixa sustentabilidade de reciclagem de lixo'

    if energia < 5:
        energiaS = 'Alta sustentabilidade de energia'
    elif energia <= 10:
        energiaS = 'Sustentabilidade moderada de energia'
    else:
        energiaS = 'Baixa sustentabilidade de energia'

    return aguaS, reciclavelS, energiaS


    
#============= INSERIR TRANSPORTE NA LISTA ======================
def transporteFuncion():
   
    transporte = []
    bic = input('Você utiliza bicicleta como meio de transporte? (S/N): ').upper()
    while bic not in ['S', 'N']:
        error()
        bic = input('Você utiliza bicicleta como meio de transporte? (S/N): ').upper()
    if bic == 'S':
        transporte.append('bicicleta')
        
    pub = input('Você utiliza transporte público? (S/N): ').upper()
    while pub not in ['S', 'N']:
        error()
        pub = input('Você utiliza transporte público? (S/N): ').upper()
    if pub == 'S':
        transporte.append('transporteP')

    caminhada = input('Você costuma fazer caminhada para ir aos lugares? (S/N):').upper()
    while caminhada not in ['S', 'N']:
        error()
        caminhada = input('Você costuma fazer caminhada para ir aos lugares? (S/N):').upper()
    if caminhada == 'S':
        transporte.append('caminhada')

    carroC = input('Você utiliza carro com combustivel fossil para se locomover? (S/N): ').upper()
    while carroC not in ['S', 'N']:
        error()
        carroC = input('Você utiliza carro com combustivel fossil para se locomover? (S/N): ').upper()
    if carroC == 'S':
        transporte.append('carroC')
        
    carroE = input('Você utiliza carro elétrico como meio de transporte? (S/N): ').upper()
    while carroE not in ['S', 'N']:
        error()
        carroE = input('Você utiliza carro elétrico como meio de transporte? (S/N): ').upper()
    if carroE == 'S':
        transporte.append('carroE')

    carona = input('Você costuma usar de carona como meio de transporte? (S/N): ').upper()
    while carona not in ['S','N']:
        error()
        carona = input('Você costuma usar de carona como meio de transporte? (S/N): ').upper()
    if carona == 'S':
        transporte.append('carona')
        
    return transporte
#================== analise transporte ======================
def analiseTransporte(transporte):
    alta = ['caminhada', 'carroE', 'bicicleta', 'transporteP']
    moderado = ['carroC', 'carona']

    if any(v in transporte for v in alta):
        sustentabilidade = 'Alta sustentabilidade em transporte'

    if any(v in transporte for v in moderado):
        sustentabilidade = 'Sustentabilidade moderada em transporte'

    if not any(v in transporte for v in alta):
        sustentabilidade = 'Baixa sustentabilidade em transporte'
    
    if transporte == []:
        sustentabilidade = 'Você não escolheu nenhum meio de transporte!'

    return sustentabilidade

#============== PRINT DAS ANALISES ===================
  
while restart == 'S':
    data = date.today()
    aguaS, reciclavelS, energiaS = consumo()
    transporte = transporteFuncion()
    sustentabilidade = analiseTransporte(transporte)
    print(f'\n{aguaS}')
    print(f'\n{reciclavelS}')
    print(f'\n{energiaS}')
    print(f'\n{sustentabilidade}')
    transporte = []
#==================== RESTART ========================

    restart = input('\nQuer fazer uma outra analise? (S/N): ').upper()
    while restart not in ['S', 'N']:
        error()
        restart = input('\nQuer fazer uma outra analise? (S/N): ').upper()
