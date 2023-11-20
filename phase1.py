#module standard de python requise pour le projet
import argparse
import json
import datetime
import requests

def analyser_commande():
    # fonction qui encapsule tous les appels au module argparse
    parser = argparse.ArgumentParser(description="Extraction de "
    "valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('symbole', nargs='+', help='Nom de symbole boursiers')
    parser.add_argument('-d', '--début', type=str, help='Date de début (format: AAAA-MM-JJ)')
    parser.add_argument('-f', '--fin', type=str, help='Date de fin (format: AAAA-MM-JJ)')
    parser.add_argument('-v', '--valeur', choices=['fermeture', 'ouverture', 'min', 'max',
    'volume'],default='fermeture', help='La valeur désirée (par défaut: fermeture)')
    return parser.parse_args()

def produire_historique(symboles, début, fin, valeur_desiree):
    #fonction qui interagir avec le serveur du cours 
    # afin de récupérer l'historique des symboles désirés
    url = f'https://pax.ulaval.ca/action/{symboles}/historique/'
    params = {
        'début': début,
        'fin': fin,
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        historique = data.get('historique', {})
        result = [(date, values[valeur_desiree]) for date, values in historique.items()]
        return result
    print(f"Erreur lors de la récupération des données pour {symboles}: {response.text}")
    return []
if __name__ == '__main__':
    args = analyser_commande()
    for symbole in args.symbole:
        date_début = args.début or args.fin
        date_fin = args.fin or str(datetime.date.today())
        historiques = produire_historique(symbole, date_début, date_fin, args.valeur)
        print(f"titre={symbole}: valeur={args.valeur}, début={date_début}, fin={date_fin}")
        print(historiques)
        