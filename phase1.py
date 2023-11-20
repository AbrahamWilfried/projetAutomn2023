import argparse
import json
import datetime
import requests

def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de " 
    "valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('symboles', nargs='+', help='Nom des symboles boursiers')
    parser.add_argument('-d', '--début', type=str, help='Date de début (format: AAAA-MM-JJ)')
    parser.add_argument('-f', '--fin', type=str, help='Date de fin (format: AAAA-MM-JJ)')
    parser.add_argument('-v', '--valeur', choices=['fermeture', 'ouverture', 'min', 'max', 'volume'],
                        default='fermeture', help='La valeur désirée (par défaut: fermeture)')
    return parser.parse_args()

def produire_historique(symboles, debut, fin, valeur_desiree):
    url = f'https://pax.ulaval.ca/action/{symboles}/historique/'
    params = {
        'début': debut,
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
    for symboles in args.symboles:
        debut = args.début or args.fin  
        fin = args.fin or str(datetime.date.today())  
        historique = produire_historique(symboles, debut, fin, args.valeur)
        print(f"titre={symboles}: valeur={args.valeur}, début={debut}, fin={fin}")
        print(historique)