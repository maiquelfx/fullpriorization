# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:51:29 2023

@author: USER
"""

msg1 = '''
import pytest
from main import Calc

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
novo_dicio = {}
ordem = 0

for teste, ordem_original in sorted(dicio.items(), key=lambda x: x[1], reverse=True):
    novo_dicio[teste] = ordens_ordenadas.index(ordem_original)


class TestSomar:
    def setup_method(self):
        self.inst = Calc()
'''

n = 20  # Número de testes
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
    
        
        teste_str = f'# teste {i}\n'
        teste_str += f'complexidade={complexidade}\n'
        teste_str += f'risco={risco}\n'
        teste_str += f'prazo={risco}\n'
        teste_str += f"dicio['t{i}'] = calc()\n"
        dados_testes_str += teste_str
        dados_testes_str += '\n'
    
    # Agora, você tem todos os dados dos testes em uma única string com quebras de linha
    
    #salvar os dados
    
    with open('gerador1.txt', 'w') as arquivo:
        arquivo.write(dados_testes_str)
        
        
    print(dados_testes_str)

##########################################
if gerador2 == 1: 
    import random
    import string
    
    #cd C:\Users\USER\Documents\Agência\Arte Atuarial\Python\Aulas\Testes Unitários\Pytest
    
    
    # Número de testes desejados
    num_inicial = 1  # Número inicial
    
    testes_str = ""  # String para armazenar os dados dos testes
     # Valor inicial
    
    for i in range(n):
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        resultado_esperado = a + b
        teste_str = f"""
    # Teste {num_inicial}
    @pytest.mark.run(order=novo_dicio.get('t{num_inicial}',0))
    def test_equal_{num_inicial}(self):
        assert self.inst.equal({a}, {b}) == {resultado_esperado}
    """
        testes_str += teste_str
        num_inicial += 1
    
    with open('gerador7.txt', 'w') as arquivo:
        try:
            arquivo.write(testes_str)
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
    
    
    print(testes_str)
##########################################

saida = msg1 + '\n' + dados_testes_str + '\n' + msg2 + '\n' + testes_str

with open('test_main_grp.py', 'w') as arquivo:
    try:
        arquivo.write(saida)
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

