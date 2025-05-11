#4. Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.
x=0
for i in range(1, 501):
    if i%2!=0 and i%3==0:
        print('+', i)
        x+=i
print(x)