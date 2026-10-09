###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
wifi = input("Introdueix el nivell de senyal Wi-Fi en dBm: ")
if (wifi >= "-50"):
    print("La cobertura Wi-Fi és excel·lent.")
elif (wifi >= "-67"):
    print("La cobertura Wi-Fi és bona.")
elif (wifi >= "-75"):
    print("La cobertura Wi-Fi és feble.")
else:
    print("La cobertura Wi-Fi és molt feble.")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
fibra = input("Introdueix la potència òptica rebuda en dBm: ")
if (fibra < "-27"):
    print("El nivell de recepció és massa baix.")
elif (fibra > "-8"):
    print("El nivell de recepció és massa alt.")
else:
    print("El nivell de recepció és acceptable.")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix el consum de dades en GB: "))
if (consum <= 20):
    print("El consum és dins del límit.")
else:
    print(f"El consum ha superat el límit en {consum - 20} GB.")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los = input("Encés?: (si/no) ")
internet = input("Encés?: (si/no) ")
if (los == "si" and internet == "si"):
    print("La connexió sembla funcionar correctament.")
elif (los == "si" and internet == "no"):
    print("Cal comprovar el servei del proveïdor.")
elif (los == "no" and internet == "sí"):
    print("Cal revisar el cable òptic")
else:
    print("Hi ha un error")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = int(input("Quanta bateria tens?: "))
if (bateria >= 50):
    print("Suficient")
elif(bateria > 20):
    print("Baix")
else:
    print("Crític")