import random

aleatorio = random.randint(1,9)
aleatorio2 = random.randint(1,9)

if aleatorio == 4 :
    print ("Te ganaste un chupete")
elif aleatorio == 8:
    print("te ganaste un balon")
elif aleatorio == 3 and aleatorio2 == 7:
    print("te ganaste un televisor")
else:
    print("te perdiste")