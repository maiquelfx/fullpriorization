# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:15:23 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:57:46 2023

@author: USER
"""

import random
import string

#cd C:\Users\USER\Documents\Agência\Arte Atuarial\Python\Aulas\Testes Unitários\Pytest
n = 250000

# Número de testes desejados
num_inicial = 1  # Número inicial

testes_str = ""  # String para armazenar os dados dos testes
 # Valor inicial
 
msg1=f'''
# -*- coding: utf-8 -*-
import time
import pytest
import ast

from main import Calc

# Lê o conteúdo do arquivo de texto (novo_dicio.txt) e avalia como um dicionário
with open('novo_dicio.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    novo_dicio = ast.literal_eval(conteudo)
class TestCalc:
    def setup_method(self):
        self.inst = Calc()
        
'''

for i in range(n):
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    resultado_esperado = a + b
    teste_str = f"""
    # Teste {num_inicial}
    def test_equal_{num_inicial}(self):
        assert self.inst.equal({a}, {b}) == {resultado_esperado}
"""
    testes_str += teste_str
    num_inicial += 1

saida = msg1 + '\n' + testes_str

with open(f'test_simple_{n}.py', 'w') as arquivo:
    try:
        arquivo.write(saida)
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")