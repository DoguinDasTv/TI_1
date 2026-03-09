A = float(input("Insira o lado A do triângulo"))
B = float(input("Insira o lado B do triângulo"))
C = float(input("Insira o lado C do triângulo"))
if A+B>C and B+C>A and A+C>B:
    if A==B==C:
        print("Esse triângulo é equilátero")
    else:
        if A==B or B==C or A==C:
            print("Esse triângulo é isóceles")
        else:
            print("Esse triângulo é escaleno")
else:
    print("Isso não é um triângulo, tente novamente")
