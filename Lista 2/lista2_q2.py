t1 = input("Texto 1? ")
t2 = input("Texto 2? ")
t3 = input("Texto 3? ")

lista = [t1.lower(), t2.lower(), t3.lower()]
lista.sort()

print("Seguem os textos em ordem:")
print("1°: "+ lista[0])
print("2°: "+ lista[1])
print("3°: "+ lista[2])