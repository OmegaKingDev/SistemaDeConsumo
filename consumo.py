from datetime import date
restart = 'S'


agua = 0

while restart == 'S':
    data = date.today()
    agua = float(input('Digite o consumo de água em litros: '))
    reciclavel = float(input('Informe a quantidade de lixo reciclável emm kg:'))
    lixo = float(input('Informe a quantidade de lixo total produzido: '))
    energia = float(input('Digite o consumo de energia em kWh: '))
    