import pytest
from main import Calc

dicio = {}

pond_comp = 0.40
pond_prio = 0.60

def calc():
    return (pond_comp * complexidade + pond_prio * prioridade)


# Teste 1
complexidade = 5
prioridade = 5
dicio['t1'] = calc()

# Teste n ... 

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

    #Teste 1 
    @pytest.mark.run(order=novo_dicio.get('t1', 0))    
    def test_equal_1(self):
        assert self.inst.equal(5, 5) == 10

    #Teste n ...  
    

   
