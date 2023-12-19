#python -m pytest -v test_main_v5.py
#python -m pytest -v -n auto test_main_v8.py


# peso_comp = 0.33 #peso1 1/3 -> equivale a peso 1
# peso_prio = 0.67 #peso2 2/3 -> equivale a peso 2 // x/3

# peso_comp = 0.40 #2/5 peso 2 // 0,80/2
# peso_prio = 0.60 #3/5  peso 3 'maior prioridade // 1,20/2

import random
import string

# Número de testes desejados
n = 10
num_inicial = 1  # Número inicial

testes_str = ""  # String para armazenar os dados dos testes
variavel_inicial = num_inicial  # Valor inicial

for i in range(n):
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    resultado_esperado = a + b
    teste_str = f"""
    # Teste {variavel_inicial}
    @pytest.mark.run(order=novo_dicio.get('t{variavel_inicial}', {variavel_inicial}))    
    def test_equal_{variavel_inicial}(self):
        assert self.inst.equal({a}, {b}) == {resultado_esperado}
"""
    testes_str += teste_str
    variavel_inicial += 1

with open('gerador2.txt', 'w') as arquivo:
    try:
        arquivo.write(testes_str)
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


print(testes_str)
