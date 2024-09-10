print("Mas sobre funciones")
# Aqui se escriben las funciones

def suma_ab(a,b):
    s=a+b
    return s

def resta_cd(c,d):
    r=c-d
    return r

def mult(e,f):
    m=e*f
    return m

def divi_gh(g,h):
    d=g/h
    return d

# Llamadas a funciones
print("calculando suma")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es igual a {suma}")

print("--- calculando resta ---")
x=int(input("Ingresa el primer numero "))
y=int(input("Ingresa el segundo numero "))
resta=resta_cd(x,y)
print(f"la suma de {x} - {y} es igual a {resta}")

print("--- calculando multiplicacion ---")
x2=int(input("Ingresa el primer numero "))
y2=int(input("Ingresa el segundo numero "))
multi=mult(x2,y2)
print(f"la suma de {x2} x {y2} es igual a {multi}\n")

print("--- calculando division ---")
x3=int(input("Ingresa el primer numero "))
y3=int(input("Ingresa el segundo numero "))
div=divi_gh(x3,y3)
print(f"la suma de {x3} / {y3} es igual a {div}")

