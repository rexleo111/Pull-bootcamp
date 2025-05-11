#6. Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário.
x= int(input('digite um numero: '))
for i in range(1, 11):
    print(i,'X', x,' =', i * x)