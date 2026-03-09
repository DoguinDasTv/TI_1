a = int(input("Insira o coeficiente a da equação"))
b = int(input("Insira o coeficiente b da equação"))
c = int(input("Insira o coeficiente c da equação"))
delta = b^2 - 4*a*c
if delta<0:
    print("Não existe X1 e X2 para esta equação")
else:
    x1 = (-(b)+delta^-2)//2*a
    x2 = (-(b)-delta^-2)//2*a
    print(f"\n\t X1 da equação será {x1:1.2f} e X2 será {x2:1.2f}")
