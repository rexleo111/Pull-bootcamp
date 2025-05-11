#A professora Ana precisa de um programa que calcule a média de três notas de um aluno
# e diga se ele foi aprovado ou reprovado. A média mínima para aprovação é 7.0.
def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 6.0:
        print(f'Aprovado, a média é, {media:.2f}')
    else:
        print(f'Reprovado, a média é , {media:.2f}')
    return media
if __name__ == '__main__':
    n1= int(input('Digite a primeira nota: '))
    n2= int(input('digite a segunda nota: '))
    n3= int(input('digite a terceira nota: '))
    calcular_media(n1, n2, n3)



