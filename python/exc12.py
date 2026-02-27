produto = float(input("Insira o valor do produto"))
desconto = float(input("Insira o valor do desconto em porcentagem"))
print(f"\n\t O valor antigo é {produto:1.2f} reais, o valor do desconto é {desconto/100*produto:1.2f} reais e o valor novo do produto é {produto-desconto/100*produto:1.2f} reais")
