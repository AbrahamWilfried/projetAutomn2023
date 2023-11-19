import argparse
import requests
import json
import datetime

def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('symboles', nargs='+', help='Nom des symboles boursiers')
    parser.add_argument('-d', '--début', type=str, help='Date de début (format: AAAA-MM-JJ)')
    parser.add_argument('-f', '--fin', type=str, help='Date de fin (format: AAAA-MM-JJ)')
    parser.add_argument('-v', '--valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'], default='fermeture', help='La valeur désirée (par défaut: fermeture)')
    return parser.parse_args()

def produire_historique(symbole, date_debut, date_fin, valeur_desiree):
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    params = {
        'début': date_debut,
        'fin': date_fin,
    }
    
    response = requests.get(url=url, params=params)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        historique = data.get('historique', {})
        result = [(date, values[valeur_desiree]) for date, values in historique.items()]
        return result
    else:
        print(f"Erreur lors de la récupération des données pour {symbole}: {response.text}")
        return []

