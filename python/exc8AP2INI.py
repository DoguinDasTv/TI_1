N = int(input("Insira um número inteiro de 3 dígitos"))
C = (N//100)
D = ((N%100)//10)*10
U = (N%10)*100
print(f"\n\t {U+D+C:1d}")
