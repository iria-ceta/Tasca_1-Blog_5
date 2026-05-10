"""
DocExercici 1 (2 punts)
Crea una funció afegir_edat_a_tots(persones, anys) que afegeixi els anys especificats a l'edat de totes les persones de la llista. Aquesta funció modifica la llista original i no retorna res. Valida que anys sigui un enter positiu.
persones = [
    {'nom': 'Anna Garcia', 'edat': 25},
    {'nom': 'Marc Puig', 'edat': 42},
    {'nom': 'Laura Martí', 'edat': 35},
    {'nom': 'Jordi Soler', 'edat': 58},
    {'nom': 'Marta Vidal', 'edat': 29}
]

def afegir_edat_a_tots(persones, anys):
    # El teu codi aquí
string for tascab2-03
"""

def afegir_edat_a_tots(persones, anys):
    if isinstance(anys, int) and anys > 0:
        for persona in persones:
            persona["edat"] += anys
                
"""
Exercici 2 (3 punts)
Escriu una funció trobar_edat_maxima(persones) que rebi una llista de diccionaris amb claus 'nom' (string) i 'edat' (int), i retorni l'edat més alta. Valida que la llista no sigui buida i que tots els diccionaris tinguin les claus correctes, sinó retorna -1. Dóna la sortida de les crides de prova.
def trobar_edat_maxima(persones):
    # El teu codi aquí

"""

def trobar_edat_maxima(persones):
    if not persones:
        return -1
    for persona in persones:
        if not isinstance(persona, dict) or "nom" not in persona or "edat" not in persona:
            return -1
        
    edats = []
    for persona in persones:
        if not isinstance(persona.get("edat"), int):
            return -1
        edats.append(persona["edat"])
    return max(edats) if edats else -1


"""
Exercici 3 (2 punts)
Fes una funció trobar_producte_mes_car() que retorni el diccionari del producte amb el preu més alt de la variable global productes. Si la llista global està buida, retorna None.
# Variable global

"""

def trobar_producte_mes_car():
    # El teu codi aquí
    global productes
    if not productes:
        return None
    
    producte_mes_car = productes[0]
    
    for producte in productes:
        if producte["preu"] > producte_mes_car["preu"]:
            producte_mes_car = producte
            
    return producte_mes_car


"""
Exercici 4 (3 punts)
Escriu una funció comptar_empleats_per_departament(empresa) que rebi una diccionari amb claus 'nom' i 'departaments' on departaments és una llista de diccionaris amb 'nom' i 'empleats', i retorni un diccionari amb el nom de cada departament i el seu número d'empleats. Fes un exemple de crida de la funció i dóna la sortida per les dades de prova empresa_de_prova.

"""
def comptar_empleats_per_departament(empresa):
    # El teu codi aqui
    departaments = {}
    for departament in empresa["departaments"]:
        departaments[departament["nom"]] = len(departament["empleats"])
    return departaments

# ========== PROVES ==========
if __name__=="__main__":
    print("=== Prova 1: ===")