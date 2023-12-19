# -*- coding: utf-8 -*-
#gerar o arquivo de saída
# python -m pytest -v test_x.py > output.txt

import re

def calcular_apdf(falhados, n):
    m = len(falhados) 
    tf_sum = sum(falhados)
    apfd = 1 - (tf_sum / (n * m)) + 1 / (2 * n)
    return apfd

def test_apfd(report_content):
    linhas_coletadas = re.search(r'collected (\d+) items', report_content)
    n = int(linhas_coletadas.group(1))

    falhados = re.findall(r'test_([\w_]+)\s*(FAILED|PASSED)', report_content)

    qtd_falhados = [i + 1 for i, (_, status) in enumerate(falhados) if status == 'FAILED']

    if qtd_falhados == []:
        print('Nenhum, não foi possível calcular')
    else:
        valor_apfd = calcular_apdf(qtd_falhados, n)
        assert 0 <= valor_apfd <= 1, f"APFD fora do intervalo: {valor_apfd}"
        print(f"Testes falhados: {qtd_falhados}")
        print(f"APFD: {valor_apfd}")

if __name__ == '__main__':
    #with open('caminho/do/meu/arquivo.txt', 'r'):
    with open('APFD/output1.txt', 'r') as file:
        report_content = file.read()

    test_apfd(report_content)
