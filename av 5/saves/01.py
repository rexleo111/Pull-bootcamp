#1. A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo. Calcule a conversão e construa o relatório de saída tabular (em forma de tabela de duas colunas) de graus Celsius em função de graus Fahrenheit que que variam de 45 a 80 de 1 em 1.
print('Fahreinheit | Celsius')
for i in range(45, 81):
    C= (5/9) * (i - 32)
    print(f'{i},ºF |, {C:.3f}, ºC')