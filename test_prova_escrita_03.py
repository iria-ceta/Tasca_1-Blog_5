import pytest
import tascab2_03   # Importem el fitxer on hi ha les funcions

# Fem servir la parametrització per provar diversos casos d'un sol cop
@pytest.mark.parametrize("llista_persones, resultat_esperat", [
    # Cas 1: Una llista normal amb edats
    ([{'nom': 'Anna', 'edat': 20}, {'nom': 'Pep', 'edat': 30}], 30),
    
    # Cas 2: Una llista buida (ha de retornar -1)
    ([], -1),
    
    # Cas 3: Una llista on falta la clau 'edat' (ha de retornar -1)
    ([{'nom': 'Anna'}], -1),
    
    # Cas 4: Una llista on l'edat no és un número (ha de retornar -1)
    ([{'nom': 'Anna', 'edat': 'vint'}], -1)
])
def test_exercici_2(llista_persones, resultat_esperat):
    """Aquest test comprova si trobem l'edat més alta correctament."""
    # Cridem a la funció
    resultat = tascab2_03.trobar_edat_maxima(llista_persones)
    # Comprovem si el resultat és el que esperàvem
    assert resultat == resultat_esperat

@pytest.mark.parametrize("productes_a_provar, nom_esperat", [
    # Cas 1: Diversos productes
    ([{'nom': 'Pa', 'preu': 1}, {'nom': 'Vi', 'preu': 10}], 'Pa'),
    
    # Cas 2: Llista buida (ha de retornar None)
    ([], None)
])
def test_exercici_3(productes_a_provar, nom_esperat):
    """Aquest test comprova quin és el producte més car."""
    # Com que la funció usa una variable global, l'hem de canviar abans de provar
    tascab2_03.productes = productes_a_provar
    
    resultat = tascab2_03.trobar_producte_mes_car()
    
    if nom_esperat is None:
        assert resultat is None
    else:
        assert resultat['nom'] == nom_esperat

@pytest.mark.parametrize("dades_empresa, diccionari_esperat", [
    # Cas 1: Una empresa amb departaments i empleats
    ({
        'departaments': [
            {'nom': 'Vendes', 'empleats': [{'nom': 'Joan'}, {'nom': 'Marta'}]},
            {'nom': 'IT', 'empleats': [{'nom': 'Pere'}]}
        ]
    }, {'Vendes': 2, 'IT': 1}),
    
    # Cas 2: Una empresa sense departaments
    ({'departaments': []}, {})
])
def test_exercici_4(dades_empresa, diccionari_esperat):
    """Aquest test comprova si comptem bé els empleats per departament."""
    resultat = tascab2_03.comptar_empleats_per_departament(dades_empresa)
    assert resultat == diccionari_esperat

