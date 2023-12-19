# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:51:29 2023

@author: USER
"""

import random
import string

# Parâmetros
num_inicial = 1  # Número inicial
n = 100  # Número de testes
pond_comp = 1
pond_prio = 1

dados_testes_str = ""  # String para armazenar os dados dos testes

for i in range(num_inicial, num_inicial + n):
    complexidade = random.randint(1, 5)
    risco = random.randint(1, 5)
    prazo = random.randint(1, 5)

    
    teste_str = f'# teste {i}\n'
    teste_str += f'complexidade={complexidade}\n'
    teste_str += f'risco={risco}\n'
    teste_str += f'prazo={risco}\n'
    teste_str += f"dicio['t{i}'] = calc()\n"
    dados_testes_str += teste_str
    dados_testes_str += '\n'

# dados dos testes em uma única string com quebras de linha

#salvar os dados

with open('gerador1.txt', 'w') as arquivo:
    arquivo.write(dados_testes_str)
    
    
print(dados_testes_str)
