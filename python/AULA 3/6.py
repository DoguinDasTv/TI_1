preço = float(input("Insira o valor do produto em reais"))
if preço>100:
    desconto = preço*0.1
    print(f"n\t O desconto será de 10%, sendo assim o produto tera um desconto de {desconto:1.2f}, custando agora {preço-desconto:1.2f}")
else:
    print("Nenhum desconto será aplicado")
