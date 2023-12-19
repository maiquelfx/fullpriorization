import pytest
from main import Calc

#todos os valores serão recalculados automaticamente
# python -m pytest -v test_arquivo.py

dicio = {}

pond_comp = 0.40
pond_prio = 0.60


def calc():
    return pond_comp * complexidade + pond_prio * risco

# grupo 1
complexidade=2
risco=3
dicio['g1'] = calc()
qg1 = 5
g1 = 1 #boolean, 1 para true / 2 para false

# grupo 2
complexidade=5
risco=4
dicio['g2'] = calc()
qg2 = 2
g2 = 1

#insira novos grupos

# Crie uma lista ordenada de valores únicos das ordens
ordens_ordenadas = sorted(set(dicio.values()), reverse=True)

# Crie um novo dicionário com as ordens atualizadas
novo_dicio = {}
ordem = 0

# novo dicio Ex.: {'g2': 0, 'g1': 1, 'g3': 2} onde g2 será testado primeiro. 
for teste, ordem_original in sorted(dicio.items(), key=lambda x: x[1], reverse=True):
    novo_dicio[teste] = ordens_ordenadas.index(ordem_original)


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
        self.inst = Calc()    #instanciamento

    if g1 == 1: 
    
        # Teste 1 grupo 1
        @pytest.mark.run(order=ordens_grupos['g1'][0])  
        def test_grupo_1_equal_1(self):
            assert self.inst.equal(38, 89) == 127

        # Teste 2 grupo 1
        @pytest.mark.run(order=ordens_grupos['g1'][1])   
        def test_grupo_1_equal_2(self):
            assert self.inst.equal(96, 90) == 186

        # Teste 3 grupo 1
        @pytest.mark.run(order=ordens_grupos['g1'][2])    
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
