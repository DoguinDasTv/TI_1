salario = float(input("Insira o salário do funcionário"))
if salario<=1500:
    print(f"\n\t O salario terá um aumento de 15%, sendo agora {salario+salario*0.15:1.2f}")
else:
    if salario>1500 and salario<=3000:
        print(f"\n\t O salario tera um aumento de 10%, sendo agora {salario+salario*0.1:1.2f}")
    else:
        print(f"\n\t O salario tera um aumento de 5%, sendo agora {salario+salario*0.05:1.2f}")
    
        
