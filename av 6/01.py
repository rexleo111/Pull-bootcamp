#Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada. A função main chama a função passando os dois argumentos lidos, ou seja, digitados pelo usuário.
def mostrar(mensagem, numero):
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

if __name__ == "__main__":
    mensagem = input("Digite uma mensagem: ")
    numero = input("Digite um numero")
    mostrar(mensagem, numero)


