###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

# i = 0
# while (i<10):
#     i += 1
#     print(i)

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

#he suposat que era realment una suma de parells 2+4+6...
# i = 0
# parells = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         parells += i
#         print(parells)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# factorial = int(input("escriu el valor del numero factorial que vols calcular: "))
# multiplicacio = 1

# while factorial > 0:
#     multiplicacio = multiplicacio * factorial 
#     factorial -= 1
# print(multiplicacio)

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

# c = input("introdueix una contrasenya de 8 caracters: ")
# while len(c) < 8:
#     print("no te 8 caràcters")
#     c = input("introdueix una contrasenya de 8 caracters: ")
# print("contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

# multiplicar = int(input("Escriu un numero enter: "))
# i = 0
# while i < 10:
#     i += 1
#     print (multiplicar * i)

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

# n = int(input("Escriu un número enter positiu: "))

# i = 2  
# while i <= n:
#     es_primer = True
#     j = 2

#     while j < i:
#         if i % j == 0:
#             es_primer = False
#             break  
#         j += 1

#     if es_primer:
#         print(i)

#     i += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

# enters = 1
# suma = 0
# while enters != 0:
#     enters = int(input("Introdueix un numero enter per fer el sumatori, si es 0 s'acaba el bucle: "))
#     suma += enters
#     print (suma)
# else:
#     print("S'ha acabat el bucle")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.


# suma = int(input("introdueix un num enter pos, !!NO INTRODUEIXIS EL 0!!: "))
# i = 1
# xifres = 1
# while (suma % i) <= 10 :
#     i *= 10
#     xifres += 1

# print(f"el teu número te {xifres - 1} xifres")


# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.



# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
secret = 7
numero = 0
while numero != secret:
    numero = int(input("escriu un numero secret: "))
    if numero > secret:
        print("El numero secret es més petit")
    else:
        print("El numero secret es més gran")  
else:
    print("!!!!!L'has encertat!!!!!!")