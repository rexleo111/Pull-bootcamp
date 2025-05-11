#Crie uma função para somar três valores. Ela recebe os três valores, calcula a soma e retorna o resultado do cálculo.A função main lê os três valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.
def soma(a,b,c):
    return a+b+c
if __name__ == '__main__':
    a = int(input('Digite um valor: '))
    b = int(input('Digite um valor: '))
    c = int(input('Digite um valor: '))
    print (soma(a,b,c))