Vc = int(input("Insira o valor da compra"))
Vp = int(input("Insira o valor pago pelo cliente"))
T = Vp-Vc
cem = T//100
cinquenta = (T-cem*100)//50
vinte = (T-(cem*100)+(cinquenta*50))//20
print(f"\n\t Troco {T:1d}R$")
print(f"\n\t R$100 {cem:1d} cédulas")
print(f"\n\t R$50 {cinquenta:1d} cédulas")
print(f"\n\t R$20 {vinte:1d} cédulas")
