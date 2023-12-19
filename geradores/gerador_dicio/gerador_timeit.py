# -*- coding: utf-8 -*-
#print("Tempo de execução: {:.6f} segundos".format(tempo_total))
"""
Created on Mon Dec  4 10:51:29 2023

@author: USER
"""
n = 250000  # Número de testes

msg1 = '''
# -*- coding: utf-8 -*-
import time
import pytest

def grt():

    dicio = {}
    
    pond_comp = 0.20
    pond_prio = 0.60
    pond_prazo = 0.20
    
    def calc():
        return (pond_comp * complexidade + pond_prio * risco + prazo * pond_prazo)
'''

msg2 = '''
    # lista ordenada de valores únicos das ordens
    ordens_ordenadas = sorted(set(dicio.values()), reverse=True)
    
    # novo dicionário com as ordens atualizadas
    global novo_dicio
    novo_dicio = {}
    ordem = 0
    
    for teste, ordem_original in sorted(dicio.items(), key=lambda x: x[1], reverse=True):
        novo_dicio[teste] = ordens_ordenadas.index(ordem_original)


'''

msg3 = '''
inicio = time.time()
grt()
fim = time.time()

tempo_total = fim - inicio
tempo_total = round(tempo_total, 15)
print(tempo_total)

txt = str(novo_dicio)

with open('novo_dicio.txt', 'w') as arquivo:
    try:
        arquivo.write(txt)
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

'''

gerador1 = 1
gerador2 = 1

import random
import string

if gerador1 == 1:

    # Parâmetros
    num_inicial = 1  # Número inicial
    pond_comp = 1
    pond_prio = 1
    
    dados_testes_str = ""  # String para armazenar os dados dos testes
    
    for i in range(num_inicial, num_inicial + n):
        complexidade = random.randint(1, 5)
        risco = random.randint(1, 5)
        prazo = random.randint(1, 5)
    
        teste_str=f'''
    #teste {i}
    complexidade={complexidade}
    risco={risco}
    prazo={risco}
    dicio['t{i}'] = calc()
        
        '''
        dados_testes_str += teste_str
    
    # Agora, você tem todos os dados dos testes em uma única string com quebras de linha
    
    #salvar os dados
        
saida = msg1 + '\n' + dados_testes_str + '\n' + msg2 + '\n' + msg3 

with open(f'test_timeit_{n}.py', 'w') as arquivo:
    try:
        arquivo.write(saida)
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

