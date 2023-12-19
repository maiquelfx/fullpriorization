# -*- coding: utf-8 -*-

from collections import deque
import pytest
from main import Calc

# Definição da função calc
def calc(complexidade, prazo, risco, pond_comp=0.40, pond_prazo=0.40, pond_risco=0.20):
    return pond_comp * complexidade + pond_prazo * prazo + risco * pond_risco

# Inicialização do dicionário de dados de teste
dicio = {}

# Adição dos dados de teste ao dicionário
# Teste 1

complexidade = 3
prazo = 3
risco = 3
qg1 = 3
#bool ativar grupo 1 true, 0 false: 
g1 = 1
dicio['g1'] = (complexidade, prazo, risco)

# Teste 2
complexidade = 4
prazo = 4
risco = 3
qg2 = 2
g2 = 1
dicio['g2'] = (complexidade, prazo, risco)


# abaixo temos a criação de duas máquinas de pilha, uma para entrada e outra para saída
pilha_entrada = deque()
pilha_saida = deque()


# aqui adicionamos os dados de entrada à pilha de entrada
for teste, ordem_original in sorted(dicio.items(), key=lambda x: x[1][1], reverse=True):
    complexidade, prazo, risco = ordem_original
    pilha_entrada.append((teste, complexidade, prazo, risco))
print(pilha_entrada)


# Nesse laço, fazemos o processamento dos dados de entrada e empilhamento dos resultados na pilha de saída
while pilha_entrada:
    teste, complexidade, prazo, risco = pilha_entrada.popleft()
    resultado = calc(complexidade, prazo, risco)
    pilha_saida.append((teste, resultado))

print(pilha_saida)

# Precisamos criar um novo novo dicionário com as ordens atualizadas
novo_dicio = {}
ordem = 0

#tratamento e ordenação a a partir da pilha de saída e indexando as informações para o novo dicionário

indices_ordenados = [i for i, (teste, resultado) in enumerate(sorted(pilha_saida, key=lambda x: x[1], reverse=True))]

for i, (teste, resultado) in enumerate(pilha_saida):
    pilha_saida[i] = (teste, indices_ordenados.index(i))

for i, (teste, resultado) in enumerate(pilha_saida):
    novo_dicio[teste] = indices_ordenados.index(i)


# Definir a posição inicial
posicao_inicial = 1

# Dicionário para armazenar as ordens
ordens_grupos = {}

# Percorrer dinamicamente todo o novo_dicio
for posicao, grupo in enumerate(sorted(novo_dicio, key=novo_dicio.get)):
    # Extrair o número do nome do grupo
    numero_grupo = grupo[1:]
    
    # Determinar a quantidade de testes para o grupo
    qtd_testes_grupo = locals()[f"qg{numero_grupo}"]
    
    # Criar a lista de ordem de testes para o grupo
    ordem_grupo = list(range(posicao_inicial, posicao_inicial + qtd_testes_grupo))
    
    # Armazenar a ordem no dicionário
    ordens_grupos[grupo] = ordem_grupo
    
    # Atualizar a posição inicial para o próximo grupo
    posicao_inicial += qtd_testes_grupo


class TestCalc:

    def setup_method(self):
        self.inst = Calc()    

    if g1 == 1: 
    
        # Teste 1 grupo 1
        @pytest.mark.run(order=ordens_grupos['g1'][1])  
        def test_grupo_1_equal_1(self):
            assert self.inst.equal(38, 89) == 127

        # Teste 2 grupo 1
        @pytest.mark.run(order=ordens_grupos['g1'][2])   
        def test_grupo_1_equal_2(self):
            assert self.inst.equal(96, 90) == 186

        # Teste 3 grupo 1
        @pytest.mark.run(order=ordens_grupos['g1'][0])    
        def test_grupo_1_equal_3(self):
            assert self.inst.equal(96, 41) == 137
        novo_dicio.pop('g1')
        
    if g2 == 1:    

        # Teste 1 Grupo 2 
        @pytest.mark.run(order=ordens_grupos['g2'][1])    
        def test_grupo_2_equal_1(self):
            assert self.inst.equal(54, 88) == 142

        # Teste 2 Grupo 2 
        @pytest.mark.run(order=ordens_grupos['g2'][0])    
        def test_grupo_2_equal_2(self):
            assert self.inst.equal(19, 14) == 33
