caixa_geral = 1000
barracas = 0

while True:
    compra = int(input('\033[40mQuantas fichas quer comprar? \033[m'))
    if compra > 1000:
            print('\033[31;40mA gente só tem 1000 fichas!\033[m')
    elif compra < 0:
            print('\033[31;40mTa querendo vender ficha???\033[m')
    else:
        break

caixa_geral += - compra

print(f'\033[32;40mTemos {caixa_geral} fichas restantes no caixa geral\033[m')

while True:
    devolucao = int(input('\033[40mQuantas fichas quer devolver para o caixa? \033[m'))
    if devolucao > compra:
            print(f'\033[31;40mVocê só pode devolver no máximo {compra} fichas!!!\033[m')
    elif devolucao < 0:
            print('\033[31;40mTa querendo comprar ficha???\033[m')
    else:
        break

caixa_geral += devolucao

print(f'\033[32;40mA quantidade de fichas que temos no caixa geral ao final da festa foi {caixa_geral} fichas!\033[m')