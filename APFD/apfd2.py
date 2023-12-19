import re

def calcular_apfd(falhados, n):
    m = len(falhados) 
    tf_sum = sum(falhados)
    apfd = 1 - (tf_sum / (n * m)) + 1 / (2 * n)
    return apfd

def test_apfd(report_content):
    linhas_coletadas = re.search(r'collected (\d+) items', report_content)
    n = int(linhas_coletadas.group(1))

    falhados = re.findall(r'test_([\w_]+)\s*(FAILED|PASSED)', report_content)

    qtd_falhados = [i + 1 for i, (_, status) in enumerate(falhados) if status == 'FAILED']

    if not qtd_falhados:
        print('Nenhum teste falhado, não foi possível calcular o APFD.')
    else:
        # Captura o índice real do teste antes do "FAILED"
        indices_reais = [i + 1 for i, (_, status) in enumerate(falhados) if status == 'FAILED']
        # Calcula a posição do teste priorizado
        posicoes_priorizadas = [i + 1 for i, (_, status) in enumerate(falhados) if status == 'PASSED']

        # Imprime os resultados
        for indice_real, posicao_priorizada in zip(indices_reais, posicoes_priorizadas):
            print(f"T{indice_real}, P{posicao_priorizada} (teste {indice_real} posição {posicao_priorizada})")

        valor_apfd = calcular_apfd(qtd_falhados, n)
        assert 0 <= valor_apfd <= 1, f"APFD fora do intervalo: {valor_apfd}"
        print(f"APFD: {valor_apfd:.4f}")

if __name__ == '__main__':
    #with open('output2.txt', 'r'):
    with open('APFD/output1.txt', 'r', encoding='utf-8') as file:
        report_content = file.read()

    test_apfd(report_content)
