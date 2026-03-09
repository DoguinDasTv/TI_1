salario_bruto = float(input("Insira seu salário bruto"))
prestação = float(input("Insira o valor da prestação de um empréstimo"))
if prestação>salario_bruto*0.3:
    print("Empréstimo negado")
else:
    tempo_de_serviço = float(input("Insira o seu tempo de serviço"))
    if tempo_de_serviço>2:
        print ("Aprovado com bônus")
    else:
        print ("Aprovado")
            
        

