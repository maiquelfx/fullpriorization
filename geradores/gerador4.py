# peso_comp = 0.33 #peso1 1/3 -> equivale a peso 1
# peso_prio = 0.67 #peso2 2/3 -> equivale a peso 2 // x/3

# peso_comp = 0.40 #2/5 peso 2 // 0,80/2
# peso_prio = 0.60 #3/5  peso 3 'maior prioridade // 1,20/2

import random
import string

# Número de testes desejados
n = 10
num_inicial = 1  # Número inicial
grupo = 2
indice = 10 #índice inicial

testes_str = ""  # String para armazenar os dados dos testes
variavel_inicial = num_inicial  # Valor inicial

for i in range(n):
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    resultado_esperado = a + b
    teste_str = f"""
    # Teste {variavel_inicial} Grupo {grupo} índice {indice}
    @pytest.mark.run(order=novo_dicio.get('g{grupo}', 0))    
    def test_grupo_{grupo}_equal_{variavel_inicial}(self):
        assert self.inst.equal({a}, {b}) == {resultado_esperado}
"""
    testes_str += teste_str
    variavel_inicial += 1
    indice += 1

#Para testes muito grandes, é recomendável salvar o arquivo em txt, pois a IDE pode paginar
with open('gerador2.txt', 'w') as arquivo:
    try:
        arquivo.write(testes_str)
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


print(testes_str)
