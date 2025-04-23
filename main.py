## Samuel Rodrigues Da Rocha Lima - 2314291027


# Entrada do usuário
valor = float(input("Coloque o valor a ser investido: R$ "))
dias_investido = int(input("Coloque o número de dias de investimento: "))


iof_table = {
    1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
    11: 63, 12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36, 20: 33,
    21: 30, 22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
}
def get_ir(dias_investido:int):
    if dias_investido <= 180:
        return 22.50
    elif dias_investido > 180 and dias_investido <= 360:
        return 20.00
    elif dias_investido > 360 and dias_investido <= 720:
        return 17.50
    else:
        return 15.00

def get_iof(dias_investido):
    dia = (dias_investido)
    if dia > 30:
        dia = 30

    return iof_table[dia]

    
def calcular_rendimento(valor, dias_investido):
    taxa_anual = 14.15/100
    taxa_diaria = taxa_anual / 365

    valor_rendido = valor

    for day in range(dias_investido):
        valor_rendido *= (1 + taxa_diaria)

    lucro_bruto = valor_rendido - valor
    iof = lucro_bruto * (get_iof(dias_investido) / 100)
    lucro_liquido = lucro_bruto - iof
    ir = lucro_liquido * (get_ir(dias_investido) / 100)

    valor_liquido = valor + lucro_liquido - ir

    print(f"\n Resultado do investimento em {dias_investido} dias:")
    print(f"Valor investido: R$ {valor:.2f}")
    print(f"Lucro bruto: R$ {lucro_bruto:.2f}")
    print(f"IOF: R$ {iof:.2f}")
    print(f"IR: R$ {ir:.2f}")
    print(f"Valor líquido final: R$ {valor_liquido:.2f}")


calcular_rendimento(valor, dias_investido)