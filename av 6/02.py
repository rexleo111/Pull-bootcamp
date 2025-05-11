#Implemente uma função que calcula a idade de uma pessoa. Ela recebe o ano de nascimento da pessoa, faz o cálculo e retorna à idade. A função principal (main) lê o ano de nascimento digitado pelo usuário, chama a função e mostra o valor retornado pela função calcula.
def v_idade(ano):
    idade = 2025 - ano
    print(idade)
if __name__ == "__main__":
    ano = int(input("Digite o ano de nascimento: "))
    v_idade(ano)