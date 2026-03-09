idade = int(input("Insira a idade do lutador"))
if idade>=18:
    peso = float(input("Insira o seu peso"))
    if peso<=80:
        print("Peso médio")
    else:
        print("Peso pesado")
else:
    print("Categoria Juvenil")
