import mysql.connector
from datetime import date
import numpy as np

def error():
    print('Valor inválido!')


def conexaobd():
    conexao = mysql.connector.connect(
        host = 'localhost',
        database = 'projeto_integrador',
        user = 'root',
        password = '6"gB"92H:|LK6'
    )

    if conexao.is_connected():
        cursor = conexao.cursor()

    return conexao, cursor

def consumo():
    agua = float(input('Digite o consumo de água em litros/dia: '))
    while agua <= 0:
        error()
        agua = float(input('Digite o consumo de água em litros/dia: '))

    reciclavel = float(input('Informe a porcentagem de lixo reciclado: '))
    while reciclavel <= 0 or reciclavel > 100:
        error()
        reciclavel = float(input('Informe a porcentagem de lixo reciclável: '))

    lixo = float(input('Informe a quantidade de lixo total produzido em kg: '))
    while lixo <= 0:
        error()
        lixo = float(input('Informe a quantidade de lixo total produzido em kg: '))

    energia = float(input('Digite o consumo de energia em kWh/dia: '))
    while energia <= 0:
        error()
        energia = float(input('Digite o consumo de energia em kWh/dia: '))




    if agua < 150:
        aguaS = 'Alta sustentabilidade'

    elif agua <= 200:
        aguaS = 'Sustentabilidade moderada'

    else:
        aguaS = 'Baixa sustentabilidade'

    if reciclavel > 50:
        reciclavelS = 'Alta sustentabilidade'

    elif reciclavel > 20:
        reciclavelS = 'Sustentabilidade moderada'
        
    else:
        reciclavelS =  'Baixa sustentabilidade'

    if energia < 5:
        energiaS = 'Alta sustentabilidade'
    elif energia <= 10:
        energiaS = 'Sustentabilidade moderada'
    else:
        energiaS = 'Baixa sustentabilidade'

    return aguaS, reciclavelS, energiaS, lixo, reciclavel, energia, agua


    

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


def analiseTransporte(transporte):
    alta = ['caminhada', 'carroE', 'bicicleta', 'transporteP']
    moderado = ['carroC', 'carona']

    if any(v in transporte for v in alta):
        sustentabilidade = 'Alta sustentabilidade'

    if any(v in transporte for v in moderado):
        sustentabilidade = 'Sustentabilidade moderada'

    if not any(v in transporte for v in alta):
        sustentabilidade = 'Baixa sustentabilidade'
    
    if transporte == []:
        sustentabilidade = 'Voce nao escolheu nenhum meio de transporte'

    return sustentabilidade


#============== PRINT DAS ANALISES ===================


def rodar():
    restart = 'S'
    while restart == 'S':
        data = date.today()
        aguaS, reciclavelS, energiaS, lixo, reciclavel, energia, agua = consumo()
        transporte = transporteFuncion()
        sustentabilidade = analiseTransporte(transporte)
        print(f'data: {data}')
        print(f'\nconsumo de água: {aguaS}')
        print(f'\nreciclagem de lixo: {reciclavelS}')
        print(f'\nuso de energia: {energiaS}')
        print(f'\nuso de transporte: {sustentabilidade}')



#============== Criptografia =========================

        alfabeto = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,'Z': 26}
    
        
        alfabetoinv = {v % 26: k for k, v in alfabeto.items()}

        key = np.array([[3, 0],
                        [2, 5]])

        def cifrar(texto):

            matriz = list(texto.replace(" ", "").upper())
            numeros = [alfabeto[letra] for letra in matriz]
            if len(numeros) % 2 != 0:
                numeros.append(alfabeto['Z'])
            resultado = []
            for i in range(0, len(numeros), 2):
                par = np.array([[numeros[i]], [numeros[i+1]]])
                cifrado = np.dot(key, par) % 26
                resultado.extend(cifrado.flatten())
            cifradoTexto =  ''.join(alfabetoinv[n] for n in resultado)

            return cifradoTexto
        
        texto_cifrado_aguastr = cifrar(aguaS)
        texto_cifrado_lixostr = cifrar(reciclavelS)
        texto_cifrado_energiastr = cifrar(energiaS)
        texto_cifrado_transportestr = cifrar(sustentabilidade)


#========================== Descriptografia ======================
        def matriz_inversa_mod26(matriz):
            determinante = int(np.round(np.linalg.det(matriz)))
            determinante_mod26 = determinante % 26

            for i in range(1, 26):
                if (determinante_mod26 * i) % 26 == 1:
                    inverso_determinante = i


            adjunta = np.array([[matriz[1][1], -matriz[0][1]],
                                [-matriz[1][0], matriz[0][0]]])


            inversa = (inverso_determinante * adjunta) % 26
            return inversa        
        
        key_inv = matriz_inversa_mod26(key)

        def descriptografar(texto):
            numeros = [alfabeto[letra] for letra in texto]
            resultado = []
            for i in range(0, len(numeros), 2):
                par = np.array([[numeros[i]], [numeros[i+1]]])
                decifrado = np.dot(key_inv, par) % 26
                resultado.extend(decifrado.flatten())
            descifradoTexto =  ''.join(alfabetoinv[n] for n in resultado)

            return descifradoTexto
        
        texto_decifrado_aguastr = descriptografar(texto_cifrado_aguastr)
        texto_decifrado_lixostr = descriptografar(texto_cifrado_lixostr)
        texto_decifrado_energiastr = descriptografar(texto_cifrado_energiastr)
        texto_decifrado_transportestr = descriptografar(texto_cifrado_transportestr)

        texto_decifrado_aguastr = descriptografar(texto_cifrado_aguastr).replace("ALTASUSTENTABILIDADE", "ALTA SUSTENTABILIDADE").replace("BAIXASUSTENTABILIDADE", "BAIXA SUSTENTABILIDADE").replace("SUSTENTABILIDADEMODERADA", "SUSTENTABILIDADE MODERADA")

        texto_decifrado_lixostr = descriptografar(texto_cifrado_lixostr).replace("ALTASUSTENTABILIDADE", "ALTA SUSTENTABILIDADE").replace("BAIXASUSTENTABILIDADE", "BAIXA SUSTENTABILIDADE").replace("SUSTENTABILIDADEMODERADA", "SUSTENTABILIDADE MODERADA")

        texto_decifrado_energiastr = descriptografar(texto_cifrado_energiastr).replace("ALTASUSTENTABILIDADE", "ALTA SUSTENTABILIDADE").replace("BAIXASUSTENTABILIDADE", "BAIXA SUSTENTABILIDADE").replace("SUSTENTABILIDADEMODERADA", "SUSTENTABILIDADE MODERADA")

        texto_decifrado_transportestr = descriptografar(texto_cifrado_transportestr).replace("ALTASUSTENTABILIDADE", "ALTA SUSTENTABILIDADE").replace("BAIXASUSTENTABILIDADE", "BAIXA SUSTENTABILIDADE").replace("SUSTENTABILIDADEMODERADA", "SUSTENTABILIDADE MODERADA")


#======================= INSERT NO BANCO DE DADOS ==================

        conexao, cursor = conexaobd()

        cursor.execute(
            "INSERT INTO analise (data, litros, porcentagem_reciclavel, lixo, energia, bicicleta, publico, caminhada, fossil, eletrico, carona, sustentabilidade_agua, sustentabilidade_lixo, sustentabilidade_energia, sustentabilidade_transporte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(data, agua,reciclavel,lixo,energia,'bicicleta' in transporte,'transporteP' in transporte,'caminhada' in transporte,'carroC' in transporte,'carroE' in transporte,'carona' in transporte,texto_cifrado_aguastr,texto_cifrado_lixostr,texto_cifrado_energiastr,texto_cifrado_transportestr))
        
        conexao.commit()
        conexao.close()
        cursor.close()
        transporte = []
    #==================== RESTART ========================

        restart = input('\nQuer fazer uma outra analise? (S/N): ').upper()
        while restart not in ['S', 'N']:
            error()
            restart = input('\nQuer fazer uma outra analise? (S/N): ').upper()

    return data





rodar()