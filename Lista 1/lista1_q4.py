texA = input("Digite o texto A: ")
texB = input("Digite o texto B: ")

mettexA = (len(texA))/2
mettexB = (len(texB))/2

print("Texto A dividido em duas Partes: " + texA[0:int(mettexA)] + " e " + texA[int(mettexA):])
print("Texto B dividido em duas Partes: " + texB[0:int(mettexB)] + " e " + texB[int(mettexB):])
print(texA[0:int(mettexA)] + " + " + texB[int(mettexB):] + " = " + texA[0:int(mettexA)]+texB[int(mettexB):])
print(texA[int(mettexA):] + " + " + texB[0:int(mettexB)] + " = " + texA[int(mettexA):]+texB[0:int(mettexB)])
print(texA[0] + " + " + texB[1] + " + " + texA[-1] + " + " + texB[-1] + " = " + texA[0]+texB[1]+texA[-1]+texB[-1])