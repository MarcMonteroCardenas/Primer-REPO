###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
switch_nom = "Marc's Switch"
switch_ubicacio = "planta baixa"
switch_ports = 5
switch_state = True;

print(f"El nom es {switch_nom}, es troba en {switch_ubicacio}, te {switch_ports} ports, i esta {switch_state}")


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_totals = 50 
gb_consumits = 20
gb_restants = gb_totals - gb_consumits
print(f"Queden {gb_restants} GB del pla de dades mòbils.")

# Actualitza el consum i recalculate els GB restants
gb_consumits = 25
gb_restants = gb_totals - gb_consumits
print(f"Queden {gb_restants} GB del pla de dades mòbils.")