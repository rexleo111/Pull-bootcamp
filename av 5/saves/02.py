#2. Melhore o programa anterior para torná-lo mais abrangente. Agora, o usuário fornecerá os valores inicial e final de graus Fahrenheit. Calcule a conversão e gere o relatório de saída tabular (em forma de tabela) considerando o intervalo digitado.
print('Fahrenheit | Celsius')
x= int(input('Digite o valor inicial de Fahrenheit: '))
y= int(input('Digite o valor final de Fahrenheit: '))
if x<=y:
    for i in range(x, y+1):
        C= (5/9) * (i - 32)
        print(f'{i}ºF | {C:.3f} ºC')

else:
    for i in range(x, y-1, -1):
        C= (5/9) * (i - 32)
        print(f'{i}ºF | {C:.3f} ºC')