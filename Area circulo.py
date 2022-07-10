import math

PI=math.pi

def areacirculo(radio):
    a = PI * (radio**2)
    return a

def volumencilindro(area, altura):
    return area * altura

r = float(input("Ingrese el valor del radio: "))
altura = float(input("Ingrese el valor de la altura "))
print("El area del circulo es :",areacirculo(2))
print("El volumen del cilindro es: ",volumencilindro(areacirculo(r),altura))
