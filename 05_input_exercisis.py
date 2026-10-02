###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic = input("introdueix el nom del tecnic: ")
nom_xarxa  = input("introduexi el nom de la xarxa: ")

print(f"el tecnic es diu {nom_tecnic} i la xarxa es diu {nom_xarxa}")


# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_fibra  = float(input("quina es la longitud de la fibra: "))
velocitat_fibra = float(input("quina es la velociata en Gbps: "))

temps = (8 / velocitat_fibra) * longitud_fibra 
print(f"El temps necessari per transmetre 1 GB de dades és de {temps} ms.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina = float(input("quantas hores de feina: "))
preu_hora = float(input("quant es el preu per hora: "))
preu_material = float(input("quant es el preu del material: "))
cost_total = (hores_feina * preu_hora) + preu_material
print(f"El cost total de la instal·lació és de {cost_total} euros.")