import random
import string

# Parâmetros
num_inicial = 1  # Número inicial
n = 4  # Número de testes
pond_comp = 1
pond_prio = 1


dados_testes_str = ""  # String para armazenar os dados dos testes

for i in range(num_inicial, num_inicial + n):
    complexidade = random.randint(1, 5)
    risco = random.randint(1, 5)
    t1 = pond_comp * complexidade + pond_prio * risco
    
    teste_str = f'# grupo {i}\n'
    teste_str += f'complexidade={complexidade}\n'
    teste_str += f'risco={risco}\n'
    teste_str += f"dicio['g{i}'] = calc()\n"
    teste_str += f"g{i} = 0\n"
    dados_testes_str += teste_str
    dados_testes_str += '\n'


with open('gerador3.txt', 'w') as arquivo:
    arquivo.write(dados_testes_str)
    
    
print(dados_testes_str)
