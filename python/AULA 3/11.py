x = float(input("Insira o X"))
y = float(input("Insira o Y"))
if x==0 and y==0:
    print("X e Y estão na origem (0,0)")
else: 
    if x==0:
        print(f"\n\t O ponto está sobre o eixo Y, na coordenada (0,{y:1.0f})")
    else:
        if y==0:
            print(f"\n\t O ponto está sobre o eixo X, na coordenada ({x:1.0f},0)")
if x>0 and y>0:
    print(f"\n\t O ponto está no quadrante 1 na coordenada ({x:1.0f},{y:1.0f})")
if x<0 and y<0:
    print(f"\n\t O ponto está no quadrante 3 na coordenada ({x:1.0f},{y:1.0f})")
if x<0 and y>0:
    print(f"\n\t O ponto está no quadrante 2 na coordenada ({x:1.0f},{y:1.0f})")
if x>0 and y<0:
    print(f"\n\t O ponto está no quadrante 4 na coordenada ({x:1.0f},{y:1.0f})")
    
