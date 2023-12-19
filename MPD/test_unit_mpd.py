# -*- coding: utf-8 -*-


from collections import deque
import pytest
from main import Calc

#cd C:\Users\USER\Documents\Ciencias Atuariais\Mestrado\PERÍODOS\1\TESTE DE SOFTWARE\SEMINÁRIO\PYTEST\GITHUB\TESTE1
# python -m pytest -v test_grupos_ind.py
# python -m pytest -v test_grupos_ind.py > subpasta/output.txt
# python -m pytest -v test_grupos_ind.py > output.txt
# python -m pytest -v test_main.py

# C:\Users\USER\Documents\Ciencias Atuariais\Mestrado\PERÍODOS\1\ESTRUTURA DE DADOS E ALGORITMOS\SEMINÁRIO\Py


# Definição da função calc
def calc(complexidade, risco, pond_comp=0.40, pond_risco=0.60):
    return pond_comp * complexidade + pond_risco * risco

# Inicialização do dicionário de dados de teste
dicio = {}

# Adição dos dados de teste ao dicionário
# Teste 1
complexidade = 3
risco = 3
dicio['t1'] = (complexidade, risco)

# Teste 2
complexidade = 4
risco = 4
dicio['t2'] = (complexidade, risco)

# Teste 3
complexidade = 3
risco = 4
dicio['t3'] = (complexidade, risco)

# Teste 4
complexidade = 5
risco = 5
dicio['t4'] = (complexidade, risco)

# abaixo temos a criação de duas máquinas de pilha, uma para entrada e outra para saída
pilha_entrada = deque()
pilha_saida = deque()

'''A pilha de entrada armazena os dados de entrada, que são os valores de complexidade e risco dos testes'''
'''Este código itera sobre o dicionário dicio, que armazena os dados de entrada. Para cada teste, o código extrai os valores de complexidade e risco da ordem original do teste e os adiciona à pilha de entrada.'''

# aqui adicionamos os dados de entrada à pilha de entrada
for teste, ordem_original in sorted(dicio.items(), key=lambda x: x[1][1], reverse=True):
    complexidade, risco = ordem_original
    pilha_entrada.append((teste, complexidade, risco))


'''A pilha de saída armazena os resultados dos testes, que são os valores retornados pela função calc.'''
'''O código para processar os dados de entrada e empilha os resultados na pilha de saída é o seguinte'''
# Nesse laço, fazemos o processamento dos dados de entrada e empilhamento dos resultados na pilha de saída
while pilha_entrada:
    teste, complexidade, risco = pilha_entrada.popleft()
    resultado = calc(complexidade, risco)
    pilha_saida.append((teste, resultado))
'''Este código itera sobre a pilha de entrada, removendo um item por vez. Para cada item, o código extrai os valores de teste, complexidade e risco e os passa para a função calc. O resultado da função calc é então adicionado à pilha de saída.'''


'''Criação de um novo dicionário com as ordens atualizadas
O código para criar um novo dicionário com as ordens atualizadas é o seguinte:'''
# Precisamos criar um novo novo dicionário com as ordens atualizadas
novo_dicio = {}
ordem = 0


#tratamento e ordenação a a partir da pilha de saída e indexando as informações para o novo dicionário

indices_ordenados = [i for i, (teste, resultado) in enumerate(sorted(pilha_saida, key=lambda x: x[1], reverse=True))]

for i, (teste, resultado) in enumerate(pilha_saida):
    pilha_saida[i] = (teste, indices_ordenados.index(i))

for i, (teste, resultado) in enumerate(pilha_saida):
    novo_dicio[teste] = indices_ordenados.index(i)


# Aqui definimos a classe de teste com as funções de setup e os testes
class TestCalc:
    def setup_method(self):
        self.inst = Calc()

    # Teste 1
    @pytest.mark.run(order=novo_dicio.get('t1', 0))    
    def test_equal_1(self):
        assert self.inst.equal(2, 71) == 73

    # Teste 2
    @pytest.mark.run(order=novo_dicio.get('t2', 0))    
    def test_equal_2(self):
        assert self.inst.equal(50, 100) == 150

    # Teste 3
    @pytest.mark.run(order=novo_dicio.get('t3', 0))    
    def test_equal_3(self):
        assert self.inst.equal(50, 60) == 110
    
    # Teste 4
    @pytest.mark.run(order=novo_dicio.get('t4', 0))    
    def test_equal_4(self):
        assert self.inst.equal(50, 65) == 115

# init opcional, o pyteste roda com ou sem
if __name__ == '__main__':
    pytest.main()
