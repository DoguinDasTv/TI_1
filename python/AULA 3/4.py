salario = float(input("Insira o salário do funcionário"))
if salario<500:
    reajuste = salario*0.15
    print(f"\n\t O reajuste será de 15%, ou seja, {reajuste:1.2f}, passando a ganhar {salario+reajuste:1.2f}")
else:
    if salario>=500 and salario<=1000:
        reajuste = salario*0.1
        print(f"\n\t O reajuste será de 10%, ou seja, {reajuste:1.2f}, passando a ganhar {salario+reajuste:1.2f}")
    else:
        reajuste = salario*0.05
        print(f"\n\t O reajuste será de 5%, ou seja, {reajuste:1.2f}, passando a ganhar {salario+reajuste:1.2f}")

